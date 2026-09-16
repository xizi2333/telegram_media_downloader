
<h1 align="center">Telegram Media Downloader</h1>

<h3 align="center">
  <a href="./README_CN.md">中文</a>
</h3>

## Overview
> Support two default running

* The robot is running, and the command `download` or `forward` is issued from the robot

* Download as a one-time download tool

### UI

#### Web page

> After running, open a browser and visit `localhost:5000`
> If it is a remote machine, you need to configure web_host: 0.0.0.0


<img alt="Code style: black" style="width:100%; high:60%;" src="./screenshot/web_ui.gif"/>

### Robot

> Need to configure `bot_token` before using the robot mode.

<img alt="Code style: black" style="width:60%; high:30%; " src="./screenshot/bot.gif"/>

### Support

| Category             | Support                                          |
| -------------------- | ------------------------------------------------ |
| Language             | `Python 3.10`                                    |
| Download media types | audio, document, photo, video, video_note, voice |

## Installation

After cloning this repository, enter its directory and create the Conda environment:

```powershell
git clone https://github.com/xizi2333/telegram_media_downloader.git
cd telegram_media_downloader
conda env create -f environment.yml
conda activate telegram
python media_downloader.py
```
