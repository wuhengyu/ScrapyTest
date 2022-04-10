# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 17:51
# @Author  : Walter
# @File    : 大规模账号池的搭建.py
# @License : (C)Copyright Walter
# @Desc    :

# 多个账号，总请求量一定的情况下，可以爬取请求分流到多个账号上
# 账号池维护100个账户信息以及对应到cookie存在数据库中，每次爬取到时候取其中一个账户到cookie

# 帐号池功能：
# 需要目标站点账号和登录后到cookie信息
# 需要定时检测cookie有效性，无效需要模拟登录生成新的cookie
# 需要一个接口随机获取cookie
# 生成cookie/检测cookie/随机提供cookie

# 帐号池架构：
# 获取模块/存储模块/检测模块/接口模块
# 存储模块
import random
import redis
# from accountpool.setting import *
