# -*- coding: utf-8 -*-
# @Time    : 2022/4/12 00:06
# @Author  : Walter
# @File    : 延时等待.py
# @License : (C)Copyright Walter
# @Desc    :
from selenium import webdriver
from selenium.webdriver.common.by import By

# 隐式等待,隐式等待会先等待一段固定时间再查找DOM，默认时间是0
# browser = webdriver.Chrome()
# browser.implicitly_wait(10)
# browser.get('https://spa2.scrape.center/')
# input = browser.find_element(by=By.CLASS_NAME, value="logo-name")
# print(input)

# 显式等待, 10秒加载出来节点属性就返回该节点
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)
browser.close()

# 等待条件
# 标题是某内容
# EC.title_is()
# 标题包含某内容
# EC.title_contains()
# 节点出现，参数是定位元组，如(By.ID, 'q')
# EC.presence_of_element_located()
# 节点可见
# EC.visibility_of()
# 所有节点都出现
# EC.presence_of_all_elements_located()
# 某个节点的文本值包含某文字
# EC.text_to_be_present_in_element()
# 某个节点值中包含某文字
# EC.text_to_be_present_in_element_value()
# 加载并切换
# EC.frame_to_be_available_and_switch_to_it()
# 节点不可见
# EC.invisibility_of_element()
# 按钮可点击
# EC.element_to_be_clickable()
# 判断一个节点是否在DOM树中
# EC.staleness_of()
# 节点可选择，参数为节点对象
# EC.element_to_be_selected()
# 节点可选择，参数为节点对象，参数为节点的定位元组
# EC.element_located_to_be_selected()
# 参数为节点对象以及状态，相等返回True，否则返回False
# EC.element_selection_state_to_be()
# 参数为定位元组以及状态，相等返回True，否则返回False
# EC.element_located_selection_state_to_be()
# 是否出现警告提示框
# EC.alert_is_present()
