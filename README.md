# はじめに
このbotはSlack上で稼働し、「Processingのスケッチを代行して画像化もしくはGIF化しチャンネルに出力する」ということを目的にPython3で書かれたものです。
processing-java、Pyhon3が実行できる環境である必要があります。

## 目次
- [環境構築](#chapter1)
    - [使用言語](#chapter1-1)
    - [Python3使用ライブラリ](#chapter1-2)
    - [インストール](#chapter1-3)

- [実行手順](#chapter2)
    - [botの作成](#chapter2-1)
    - [botの設定](#chapter2-2)
    - [botの起動](#chapter2-3)

- [Author](#chapter3)

- [開発について](#chapter4)

- [License](#chapter5)


<a id="chapter1"></a>

# 環境構築

**bashが使用できる前提で進めていきます。**

<a id="chapter1-1"></a>

## 使用言語
- Python3.7.4 (3.x~ならおそらく動きます)
- Processing (processing-javaのインストールに必要です)

<a id="chapter1-2"></a>

## python3使用ライブラリ
- [slackbot](https://github.com/lins05/slackbot) 0.5.6
- [Pillow](https://pillow.readthedocs.io/en/stable/) 7.1.2

<a id="chapter1-3"></a>

## インストール
Processingを起動して「ツール」>「"processing-java"のインストール」をクリックしprocessing-javaをインストールしてください

```bash
$ which processing-java # パスが帰ってきたらインストール済

$ pip list # インストール済のライブラリの確認

# リストに無ければ各ライブラリをインストール
$ pip install slackbot
$ pip install Pillow
```

<a id="chapter2"></a>

# 実行手順
はじめに`git clone https://github.com/kota-shiokara/processing-slackbot.git`でこのリポジトリをクローンしてください。

<a id="chapter2-1"></a>

## botの作成
botの作成を行います。[こちら](https://my.slack.com/services/new/bot)のページからbotを作成します。
APIトークンの取得を行い、設定を保存してください。トークンを忘れた場合は`https://<ワークスペースのURL>/apps`のページからボットインテグレーションを探してください。

<a id="chapter2-2"></a>

## botの設定
processing-slackbotフォルダに`slackbot_settings.py`、`sketch`フォルダ及びその中に`sketch.pde`ファイルを作成してください。その後`slackbot_settings.py`を以下のように書いていきます。

slackbot_settings.py:

```python
API_TOKEN = "<your-api-token>"
PLUGINS = ['plugins']
```

sketchファイルは空のままにしておきます。下記のような構造であれば進めて構いません。

```
processing-slackbot       # プログラムをまとめる<任意の文字列>ディレクトリ
├─ run.py                 # bot起動のためのメインファイル
├─ slackbot_settings.py   # botに関する設定を書くファイル
├─ plugins                # botの機能はこのディレクトリに追加する
   ├─ __init__.py         # 空で置いておくモジュールを示すためのファイル
   └─ func.py             # 機能を書くファイル
└─ sketch
   └─ sketch.pde          # 一旦書き込むスケッチファイル。空でOK
```

<a id="chapter2-3"></a>

## botの起動
botの起動のため`run.py`をbashで叩いて走らせます。

```bash
$ python3 run.py
```

その後、slack側でbotが入ってるチャンネルに`!output --<pngもしくはgif>`を1行目につけてprocessingのコードを投稿してください。
- pngの例

<img width="500" alt="png" src="https://user-images.githubusercontent.com/50353938/84533388-ff2f3a80-ad22-11ea-8839-b56323610076.png">

- gifの例

![gif](https://user-images.githubusercontent.com/50353938/84533112-73b5a980-ad22-11ea-8be7-43886afdb9ab.gif)

<a id="chapter3"></a>

# Author
- [kota-shiokara](https://github.com/kota-shiokara)
- Email: ikanoshiokara.fun@gmail.com
- Twitter: [@shiokara_create](https://twitter.com/shiokara_create)

<a id="chapter4"></a>

# 開発について
バグの報告、改善の要望につきましては[issue](https://github.com/kota-shiokara/processing-slackbot/issues)もしくは上記連絡先にお願いします。
[更新履歴はこちら](version.md)

<a id="chapter5"></a>

# License
[MIT License](https://choosealicense.com/licenses/mit/)

