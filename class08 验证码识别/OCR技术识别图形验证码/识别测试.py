# -*- coding: utf-8 -*-
# @Time    : 2022/4/14 00:44
# @Author  : Walter
# @File    : 识别测试.py
# @License : (C)Copyright Walter
# @Desc    :
import tesserocr
from PIL import Image
import numpy as np

image1 = Image.open('图片验证码1.png')
resuilt1 = tesserocr.image_to_text(image1)
print(resuilt1)

image2 = Image.open('图片验证码2.png')
resuilt2 = tesserocr.image_to_text(image2)
print(resuilt2)

image3 = Image.open('数字验证码.png')
resuilt3 = tesserocr.image_to_text(image3)
print(image3)
print(resuilt3)
print(tesserocr.file_to_text('数字验证码.png'))

