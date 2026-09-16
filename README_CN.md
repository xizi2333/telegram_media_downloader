
<h1 align="center">电报资源下载</h1>

<h3 align="center">
  <a href="./README.md">English</a>
</h3>

## 概述

> 支持两种默认运行

* 机器人运行，从机器人下发命令`下载`或者`转发`

* 作为一个一次性的下载工具下载

### 界面

#### 网页

> 运行后打开浏览器访问`localhost:5000`
> 如果是远程机器需要配置web_host: 0.0.0.0


<img alt="Code style: black" style="width:100%; high:60%;" src="./screenshot/web_ui.gif"/>

### 机器人

> 使用机器人模式前需要配置 `bot_token`。

<img alt="Code style: black" style="width:60%; high:30%; " src="./screenshot/bot.gif"/>

### 支持

| 类别         | 支持                                     |
| ------------ | ---------------------------------------- |
| 语言         | `Python 3.10`                             |
| 下载媒体类型 | 音频、文档、照片、视频、video_note、语音 |

## 安装

克隆仓库后进入项目目录，创建 Conda 环境：

```powershell
git clone https://github.com/xizi2333/telegram_media_downloader.git
cd telegram_media_downloader
conda env create -f environment.yml
conda activate telegram
python media_downloader.py
```
