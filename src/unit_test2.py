# -*- encoding: utf-8 -*-
#BearSki 测试类
'''
@File    :   test.py
@Time    :   2020/01/30 23:29:00
@Author  :   chenjiusi 
'''
import time
import json
from BearSki.utils.logger import SkiLogger
import os
from BearSki.case.TestRunnerSet import *
from BearSki.utils.arguments import runArg
logger=SkiLogger("test")
class test_BearSki(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass
        
    @classmethod
    def tearDownClass(cls):

        pass
        
    def setUp(self):
        # 每条case的前置条件
        pass
    def tearDown(self):
        #这是每条case的后置条件
        pass

    def test_Argments(self):

        runArg()
    
if __name__=='__main__':

    report_type=input("run alltest ?(y or n):")
    if report_type== "y":
        unittest.main()
    else:
        suite = unittest.TestSuite()
        suite.addTest(test_BearSki('factory_test'))
        unittest.TextTestRunner().run(suite)