# processing-slackbot
A Slack bot that turns a Processing sketch into a GIF or png

# はじめに
このbotはSlack上で稼働し、「Processingのスケッチを代行して画像化もしくはGIF化しチャンネルに出力する」ということを目的にPython3で書かれたものです。
processing-java、Pyhon3が実行できる環境である必要があります。また、bashが使用できることを前提に進めていきます。

# 目次
- 環境構築
    - [使用言語](#chapter1-1)
    - [Python3使用ライブラリ](#chapter1-2)
    - [インストール](#chapter1-3)

- 実行手順
    - [botの作成](#chapter2-1)

# 環境構築

<a id="chapter1-1"></a>

## 使用言語
- Python3.7.4 (3.x~ならおそらく動きます)
- Processing (processing-javaのインストールに必要です)

<a id="chapter1-2"></a>

## python3使用ライブラリ
- slackbot 0.5.6
- Pillow 7.1.2

<a id="chapter1-3"></a>

## インストール
Processingを起動して「ツール」>「"processing-java"のインストール」をクリックしprocessing-javaをインストールしてください

```bash

$ processing-java --help # ヘルプコマンド。これで説明が出てきたらインストール済

```

ライブラリはpipでインストールしてください

```bash

$ pip install slackbot
$ pip install Pillow

$ pip list # インストール済のライブラリの確認

```

# 実行手順
<a id="chapter2-1"></a>

## botの作成
はじめにbotの作成を行います。