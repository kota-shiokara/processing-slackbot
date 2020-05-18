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
def processing(message, arg):
    text = message.body['text']
    print(text)
    print(arg)
    message.send('wait...')