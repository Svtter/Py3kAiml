#!/usr/bin/env python3
# coding: utf-8

from flask import Flask, request
from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage, EventMessage, VoiceMessage
from simple import AnswerBot


TOKEN = 'pyconsult'

conf = WechatConf(
    token=TOKEN,
    appid='wxaf0b5ec4550fe5ff',
    appsecret='f4ea67a3517d76bfed746d20c42a0c9a',
    encrypt_mode='compatible',  # 可选项：normal/compatible/safe，分别对应于 明文/兼容/安全 模式
    encoding_aes_key='824wA48OdU3L1aUArK5kG6OOJCJ42qZ3P64vW9i082f'
    # 如果传入此值则必须保证同时传入 token, appid
)

wechat = WechatBasic(conf=conf)
bot = AnswerBot()
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def handle():
    if request.method == 'GET':
        return checkValid()

    # 解析本次请求的 XML 数据
    try:
        wechat.parse_data(request.data)
    except ParseError:
        print(request.data)
        print('Invalid Body Text')
        return 'error', 404

    # 获取解析好的微信请求信息
    message = wechat.get_message()

    # 关注事件以及不匹配时的默认回复
    response = handleMessage(message)
    return response


# 检查是否合法
def checkValid():
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')

    if wechat.check_signature(signature=signature,
                              timestamp=timestamp, nonce=nonce):
        return request.args.get('echostr')
    else:
        return 'false', 404


# 处理Message
def handleMessage(message):
    response = wechat.response_text(
        content=("我暂时不支持这个功能，请以反馈为开头"
                 "我将提醒我的开发者讲这个问题加入到答案中去"))

    if isinstance(message, TextMessage):
        # 当前会话内容
        content = message.content.strip()
        reply_text = bot.textin(content)
        if reply_text == '':
            reply_text = '我暂时不支持这个功能，请以“反馈”为开头我将提醒我的开发者讲这个问题加入到答案中去'
        response = wechat.response_text(content=reply_text)

    elif isinstance(message, EventMessage):
        if wechat.message.type == 'subscribe':  # 关注事件(包括普通关注事件和扫描二维码造成的关注事件)
            reply_text = '感谢您的关注！你可以回复任意内容开始聊天，或者试试语音'

        response = wechat.response_text(content=reply_text)

    elif isinstance(message, VoiceMessage):
        recognition = wechat.message.recognition
        reply_text = bot.textin(recognition)
        if reply_text == '':
            reply_text = '我暂时不支持这个功能，请以“反馈”为开头我将提醒我的开发者讲这个问题加入到答案中去'

        response = wechat.response_text(content=reply_text)

    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
