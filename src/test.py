# -*- encoding: utf-8 -*-
#BearSki 测试类
'''
@File    :   test.py
@Time    :   2020/01/30 23:29:00
@Author  :   chenjiusi 
'''

# coding=utf-8
import time
import unittest
from  BearSki import *
import json
import subprocess
from unittest import mock
from BearSki.utils.logger import SkiLogger

logger=SkiLogger("test")
class test_BearSki(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 所有case的前置条件
        subprocess.run(['python','runcmd.py','createproject','-pn','tempproject'])
        
    @classmethod
    def tearDownClass(cls):
        # 所有case的后置条件
        subprocess.run(['rm','-rf','tempproject'])
        logger.info('清除测试项目')
        
    def setUp(self):
        # 每条case的前置条件
        pass
    def tearDown(self):
        #这是每条case的后置条件
        pass
    def testBearCLI(self): 
        result = subprocess.run(['python','runcmd.py','-h'],stderr=subprocess.PIPE,stdout=subprocess.PIPE)
        # result = subprocess.run(['python','test1.py','-v'],stderr=subprocess.PIPE,stdout=subprocess.PIPE,check=True)
        # 非正常终止时候如果check=True 将不会输入出错误信息，仅提示错误
        # 测试命令行代码帮助信息
        self.assertIn('createproject', str(result.stdout))
        # logger.info(result.stdout)
    @unittest.skip('不执行case:') # 跳过这条case
    def testskipcase(self): 
        print('这是被跳过不执行的用例')

if __name__=='__main__':

    report_type=input("run alltest ?(y or n):")

    if report_type== "y":
        unittest.main()
    else:
        suite = unittest.TestSuite()
        suite.addTest(test_BearSki('testBearCLI'))
        unittest.TextTestRunner().run(suite)