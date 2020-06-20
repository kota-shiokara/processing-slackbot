import glob
import os
import os.path
import subprocess
import sys
import time
import pathlib

from PIL import Image

from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
from slackbot.bot import listen_to  # チャネル内発言で反応するデコーダ
from slackbot.bot import respond_to  # @botname: で反応するデコーダ


@listen_to('!exit')  # exitコマンド:プロセスを終了する
def kill_process(message):
    message.send('See you!')
    print('process finished')
    os._exit(10)  # プロセスの強制終了


@listen_to('!output (.*)')
def output(message, arg):  # argはオプション
    # 送信されたテキストを整形
    tmp = message.body['text']
    tmp = tmp.replace("&lt;", "<")
    tmp = tmp.replace("&gt;", ">")

    # pde上書き用の文字列に整形
    pdeCode = shaping_code(tmp.strip("!output " + arg + "\n"), arg)
    message.send('wait...')

    # pdeに上書き
    sketch_dir = pathlib.Path('./sketch')
    if not sketch_dir.exists():
        sketch_dir.mkdir()  # sketchディレクトリが無い時に生成
    print(pdeCode)
    with open('sketch/sketch.pde', 'w') as f:
        f.write(pdeCode)

    # processingの実行
    sketch_path = '--sketch=' + os.path.abspath('./sketch')
    cp = subprocess.run(
        ['processing-java',  sketch_path, '--run'])
    if cp.returncode != 0:  # processingの実行失敗時の処理
        message.send('Run is failed. Please send your sketch again.')
        return

    upload_sequence(message, arg)  # upload処理


def shaping_code(code, option):
    if option == '--png':  # pngオプション
        pictFunc = "  if((frameCount <= 15) && (frameCount % 15 == 0)) saveFrame(\"####.png\");\n  else if(frameCount > 15) exit();"
    elif option == '--gif':  # gifオプション
        pictFunc = "  if((frameCount <= 300) && (frameCount % 15 == 0)) saveFrame(\"####.png\");\n  else if(frameCount > 300) exit();"
    else:  # デフォルトではpngで返す
        pictFunc = "  if((frameCount <= 15) && (frameCount % 15 == 0)) saveFrame(\"####.png\");\n  else if(frameCount > 15) exit();"
    return code.replace("void draw(){", "void draw(){\n" + pictFunc)


def upload_sequence(message, option):
    if option == '--png':  # pngオプション
        message.channel.upload_file(
            fname="sketch/0015.png", fpath="sketch/0015.png")
        for p in glob.glob('sketch/*.png'):
            if os.path.isfile(p):
                os.remove(p)
    elif option == '--gif':  # gifオプション
        time.sleep(6)
        file_list = sorted(glob.glob('sketch/*.png'))
        images = list(map(lambda file: Image.open(file), file_list))
        images[0].save('sketch/output.gif', save_all=True,
                       append_images=images[1:], duration=400, loop=0)
        if os.path.exists('sketch/output.gif'):
            message.channel.upload_file(
                fname="sketch/output.gif", fpath="sketch/output.gif")
            for p in glob.glob('sketch/*.png'):
                if os.path.isfile(p):
                    os.remove(p)
            os.remove('sketch/output.gif')
    else:  # デフォルトではpngでupload
        message.channel.upload_file(
            fname="sketch/0015.png", fpath="sketch/0015.png")
        for p in glob.glob('sketch/*.png'):
            if os.path.isfile(p):
                os.remove(p)
