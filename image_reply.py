# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import random
import datetime

import boto3
from botocore.config import Config

# logger setup
import logging
from logging import getLogger, StreamHandler, Formatter
logger_name = "happy-snap"
logger = getLogger(logger_name)
logger.setLevel(logging.DEBUG)
stream_handler = StreamHandler()
stream_handler.setLevel(logging.DEBUG)
handler_format = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(handler_format)
logger.addHandler(stream_handler)
logger.debug("logger setting finished")

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', None)
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', None)
AWS_REGION_NAME = os.getenv('AWS_REGION_NAME', None)
AWS_S3_BUCKET_NAME = os.getenv('AWS_S3_BUCKET_NAME', None)

USE_PROXY = os.getenv('USE_PROXY', None)

logger.debug("GOT AWS ENV")

# s3 enviroment setting
session = boto3.session.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                                region_name=AWS_REGION_NAME)

if USE_PROXY:
    s3 = session.resource('s3', config=Config(proxies={'https': 'proxy.mei.co.jp:8080'}))
else:
    s3 = session.resource('s3')

bucket = s3.Bucket(AWS_S3_BUCKET_NAME)
s3_url = "https://s3-{}.amazonaws.com/{}/".format(AWS_REGION_NAME, AWS_S3_BUCKET_NAME)

logger.debug("Complete S3 handler")

def scoringImage(img_url, img_path):
    logger.debug("start scoring Image func")
    # TODO implement
    return random.randint(0, 100)


def createReply(img_path):
    logger.debug("start create reply func")
    timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    # ex "images/20140102-030405.jpg"
    img_name = "{}.jpg".format(timestamp)
    img_url = saveImage(img_path, img_name)
    score = scoringImage(img_url, img_path)
    saveScore(score, img_name)
    reply_str = "your score is {}\n".format(score)
    reply_str += "http://happy-snap.s3-website-us-east-1.amazonaws.com"
    return reply_str


def saveImage(img_path, img_name):
    logger.debug("start save image func")
    raw_name = "images/" + img_name

    bucket.upload_file(img_path, Key=raw_name)
    raw_url = s3_url + raw_name
    return raw_url


def saveScore(score, img_name):
    contents = str('{}, {}'.format(img_name, score))
    file_name = "scores/{}.txt".format(img_name)
    obj = bucket.Object(file_name)
    obj.put(
        Body=contents.encode('utf-8'),
        ContentEncoding='utf-8',
        ContentType='text/plane'
    )
    return contents


def test():
    logger.debug("start test func")
    print(createReply('sampleimage/face_sample.jpg'))
    logger.debug("end test func")


if __name__ == "__main__":
    test()
