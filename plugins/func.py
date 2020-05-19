from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
import sys

@listen_to('!exit') # 使い物にならない関数
def kill_process(message):
    message.send('See you!')
    print('process finished')
    sys.exit()

@listen_to('!processing (.*)')
def processing(message, arg): # argはオプション
    # 送信されたテキストを整形
    tmp = message.body['text']
    tmp = tmp.replace("&lt;", "<")
    tmp = tmp.replace("&gt;", ">")

    print(tmp)

    pdeCode = shaping_code(tmp.strip("!processing " + arg + "\n"), arg) # pde上書き用の文字列に整形
    #print(pdeCode)
    message.send('wait...')

    # pdeに上書き
    f = open('sketch/sketch.pde', 'w')
    f.write(pdeCode)
    f.close()

    



def shaping_code(code, option):
    if option == '--png': # pngオプション
        pictFunc = "  if((frameCount <= 15) && (frameCount % 15 == 0)) saveFrame(\"####.png\");\n  else exit();"
    else: # デフォルトの動画オプション
        pictFunc = "  if((frameCount <= 600) && (frameCount % 15 == 0)) saveFrame(\"####.png\");\n  else exit();"
    return code.replace("void draw(){", "void draw(){\n" + pictFunc)
