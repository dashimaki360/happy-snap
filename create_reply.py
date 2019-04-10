# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import random

RESPONSE_DICT = {
        'おはよう': 'おはよ!写真を撮って送ってね',
        'おはよ': 'おはよ!写真を撮って送ってね',
        'おはー': 'おはよ!写真を撮って送ってね',
        'こんにちわ': 'こんにちわ!写真を撮って送ってね',
        'こんにちは': 'こんにちわ!写真を撮って送ってね',
        "いまなんじ": "がめんのうえのほうにかいてあるよ↑↑",
        "今なんじ": "がめんのうえのほうにかいてあるよ↑↑",
        "いま何時": "がめんのうえのほうにかいてあるよ↑↑",
        "今何時": "がめんのうえのほうにかいてあるよ↑↑",
    }
FIX_REPLY_LIST = [
    "写真をおくってね",
]


def detectMsg(msgs):
    if isinstance(msgs, list):
        det_msgs = []
        for msg in msgs:
            if isinstance(msg, list):
                msg = random.choice(msg)
            det_msgs.append(msg)
        reply = det_msgs
    else:
        reply = msgs
    return reply


def dictMsg(msg):
    for dictKey in RESPONSE_DICT.keys():
        if dictKey.lower() in msg.lower():
            value = RESPONSE_DICT[dictKey]
            # check value is list or nor and rand choice
            reply = detectMsg(value)
            return reply

    reply = random.choice(FIX_REPLY_LIST)
    return reply


def createReply(txt_msg):
    reply = dictMsg(txt_msg)
    return reply
