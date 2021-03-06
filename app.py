# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys
import random
import tempfile

import create_reply
import image_reply

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    StickerMessage, StickerSendMessage,
    ImageMessage, ImageSendMessage,
)


app = Flask(__name__)

# LINE BOT setting
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    reply = "Please send me a PHOTO"

    text_msgs = TextSendMessage(text=reply)

    line_bot_api.reply_message(
        event.reply_token,
        text_msgs
    )


@handler.add(MessageEvent, message=StickerMessage)
def message_sticker(event):
    sticker_id = random.randint(180, 307)
    if sticker_id < 260:
        package_id = 3
    else:
        package_id = 4

    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(
            package_id=package_id,
            sticker_id=sticker_id,
        )
    )


@handler.add(MessageEvent, message=ImageMessage)
def message_image(event):
    # TODO
    # save image to temp path
    message_content = line_bot_api.get_message_content(event.message.id)
    with tempfile.NamedTemporaryFile(delete=True) as tf:
        for chunk in message_content.iter_content():
            tf.write(chunk)
        tempfile_path = tf.name

        reply = image_reply.createReply(tempfile_path)
        text_msgs = TextSendMessage(text=reply)
        line_bot_api.reply_message(
            event.reply_token,
            text_msgs
        )


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

