"""Tests for resumable media downloads."""

import asyncio
import os
import tempfile
import unittest

import pyrogram

from media_downloader import _check_download_finish
from module.pyrogram_extension import HookClient


CHUNK_SIZE = 1024 * 1024


class DownloadResumeTestCase(unittest.TestCase):
    """Test partial-file preservation and chunk-aligned resuming."""

    def setUp(self):
        self.loop = asyncio.new_event_loop()

    def tearDown(self):
        self.loop.close()

    def test_partial_file_is_preserved_after_size_check(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            download_path = os.path.join(temp_dir, "video.mp4")
            with open(download_path, "wb") as download_file:
                download_file.write(b"partial")

            with self.assertRaises(
                pyrogram.errors.exceptions.bad_request_400.BadRequest
            ):
                _check_download_finish(1024, download_path, "video.mp4")

            self.assertEqual(os.path.getsize(download_path), len(b"partial"))

    def test_download_resumes_from_existing_chunk(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_name = "video.mp4"
            download_path = os.path.join(temp_dir, file_name)
            with open(download_path, "wb") as download_file:
                download_file.write(b"a" * CHUNK_SIZE)

            offsets = []
            client = object.__new__(HookClient)

            async def get_file(
                _file_id, _file_size, _limit, offset, _progress, _progress_args
            ):
                offsets.append(offset)
                yield b"b" * CHUNK_SIZE

            client.get_file = get_file
            packet = (
                object(),
                temp_dir,
                file_name,
                False,
                CHUNK_SIZE * 2,
                None,
                (),
            )

            result = self.loop.run_until_complete(client.handle_download(packet))

            self.assertEqual(result, download_path)
            self.assertEqual(offsets, [1])
            self.assertEqual(os.path.getsize(download_path), CHUNK_SIZE * 2)
            with open(download_path, "rb") as download_file:
                self.assertEqual(download_file.read(1), b"a")
                download_file.seek(CHUNK_SIZE)
                self.assertEqual(download_file.read(1), b"b")

    def test_request_timeout_is_configurable(self):
        client = HookClient("request-timeout-test", request_timeout=42)

        self.assertEqual(client.REQUEST_TIMEOUT, 42)


if __name__ == "__main__":
    unittest.main()
