# -*- encoding: utf-8 -*-
'''
@File    :   initdata.py
@Time    :   2020/02/02 17:36:00
@Author  :   chenjiusi 
'''
from utest.keywords.login import login
#测试项目执行初始化数据
def initData():
    print("in initData")
    login({
            "password": "AgaveTest@5567",
            "username": "admin"
        })
def clear():
    print("in initData clear")
    