"""Tests for the custom chat history generator."""

import asyncio
import unittest
from unittest import mock

from module.get_chat_history_v2 import get_chat_history_v2


class MockMessage:
    """Minimal message object used by the history tests."""

    def __init__(self, message_id):
        self.id = message_id


class MockClient:
    """Client exposing the fallback API used by the old implementation."""

    def __init__(self):
        self.fallback_called = False

    async def get_chat_history(self, _chat_id):
        self.fallback_called = True
        yield MockMessage(3)
        yield MockMessage(2)
        yield MockMessage(1)


class GetChatHistoryV2TestCase(unittest.TestCase):
    """Test the empty-page behavior."""

    def setUp(self):
        self.loop = asyncio.new_event_loop()

    def tearDown(self):
        self.loop.close()

    async def collect_history(self, client):
        return [
            message
            async for message in get_chat_history_v2(client, chat_id=123, offset_id=0)
        ]

    def test_empty_chunk_returns_without_fallback_history(self):
        client = MockClient()

        async def empty_chunk(**_kwargs):
            return []

        with mock.patch(
            "module.get_chat_history_v2.get_chunk_v2", new=empty_chunk
        ):
            messages = self.loop.run_until_complete(self.collect_history(client))

        self.assertEqual(messages, [])
        self.assertFalse(client.fallback_called)
