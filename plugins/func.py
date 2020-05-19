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
    tmp = message.body['text']
    pdeCode = tmp.strip("!processing " + arg + "\n")
    print(pdeCode)
    message.send('wait...')
    pictFunc = "if((frameCount <= 600) && (frameCount % 15 == 0)) saveFrame(\"####.png\");\nelse exit();"
    calcCode = pdeCode.replace("void draw(){", "void draw(){\n" + pictFunc)