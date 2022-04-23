# -*- coding: utf-8 -*-
# @Time    : 2022/4/18 02:11
# @Author  : Walter
# @File    : 处理验证码.py
# @License : (C)Copyright Walter
# @Desc    :
import numpy as np
import tesserocr
from PIL import Image

image = Image.open('数字验证码2.png')
image.convert('L')
threshold = 50
print(type(image))
array = np.array(image)
print(type(array))
# 对数组筛选和处理，灰度大于50阀值对图片设置255白色，否则0黑色
array = np.where(array > threshold, 255, 0)
image = Image.fromarray(array.astype('uint8'))
image.show()
print(tesserocr.image_to_text(image))
