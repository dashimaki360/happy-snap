# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import random
import datetime

import cv2
import boto3

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', None)
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', None)
AWS_REGION_NAME = os.getenv('AWS_REGION_NAME', None)
AWS_S3_BUCKET_NAME = os.getenv('AWS_S3_BUCKET_NAME', None)

# s3 enviroment setting
session = boto3.session.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                                region_name=AWS_REGION_NAME)
s3 = session.resource('s3')
bucket = s3.Bucket(AWS_S3_BUCKET_NAME)
s3_url = "https://s3-{}.amazonaws.com/{}/".format(AWS_REGION_NAME, AWS_S3_BUCKET_NAME)

# face mask app setting
CASCADE_PATH = "haarcascade_frontalface_default.xml"
mask = cv2.imread("sampleimage/shirotan.jpg")


def scoringImage(img):
    # TODO implement
    return random.randint(0, 100)


def createReply(img_f_name, id):
    img = cv2.imread(img_f_name)
    score = scoringImage(img)
    org_url, prev_url = saveImage(img, score)
    reply_str = "your score is {}".format(score)
    return reply_str


def saveImage(raw_img, score):
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    # ex "images/068_20140102-030405.jpg"
    raw_name = "images/{:0=3}_{}.jpg".format(score, timestamp)

    tmp = "temp.jpg"
    cv2.imwrite(tmp, raw_img)
    bucket.upload_file(tmp, Key=raw_name)
    raw_url = s3_url + raw_name
    return raw_url

def test():
    print(createReply('sampleimage/face_sample.jpg', "123456789"))


if __name__ == "__main__":
    test()
