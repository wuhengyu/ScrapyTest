# -*- coding: utf-8 -*-
# @Time    : 2022/4/18 04:34
# @Author  : Walter
# @File    : 识别实战.py
# @License : (C)Copyright Walter
# @Desc    :
import re
from io import BytesIO
import tesserocr
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import numpy as np
from PIL import Image
from retrying import retry

def preprocess(image):
    image = image.convert('L')
    array = np.array(image)
    array = np.where(array > 50, 255, 0)
    image = Image.fromarray(array.astype('uint8'))
    return image

@retry(stop_max_attempt_number=30, retry_on_result=lambda x: x is False)
def login():
    browser.get('https://captcha7.scrape.center/')
    browser.find_element(by=By.CSS_SELECTOR, value='.username input[type="text"]').send_keys('admin')
    browser.find_element(by=By.CSS_SELECTOR, value='.password input[type="password"]').send_keys('admin')
    captcha = browser.find_element(by=By.CSS_SELECTOR, value='#captcha')
    image = Image.open(BytesIO(captcha.screenshot_as_png))
    image = preprocess((image))
    captcha = tesserocr.image_to_text(image)
    captcha = re.sub('[^A-Za-z0-9]', '', captcha)
    browser.find_element(by=By.CSS_SELECTOR, value='.captcha input[type="text"]').send_keys(captcha)
    browser.find_element(by=By.CSS_SELECTOR, value='.login').click()
    try:
        demo = WebDriverWait(browser, 20, 2).until(EC.presence_of_element_located(By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div/h2'))
        print(demo)
        # WebDriverWait(browser, 10).until(EC.presence_of_element_located(By.XPATH, '//h2[contains(., "登录成功")]'))
        time.sleep(10)
        browser.close()
        return True
    except TimeoutException:
        return False

if __name__ == '__main__':
    browser = webdriver.Chrome()
    login()