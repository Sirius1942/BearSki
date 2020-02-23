# coding=utf-8
import time
import unittest
from BearSki.core import Ski
from BearSki.core import DT
from BearSki.keywords.DataTreating import BaseDataTreating

import logging
import json

class atest_auth_login(unittest.TestCase,Ski):

    def setUp(self):
        self.logger=logging.getLogger("atest_auth_login")
    def tearDown(self):
        pass
    @Ski.case()
    def case_auth_login(self):
        model_name="auth_login"
        self.logger.info("in case_auth_login")
        mjstr=DT.json(model_name+'_model.json')
        res=self.step("requestFromModel",mjstr)
        jstr=DT.json(model_name+"_res.json")
        self.assertEqual(jstr['status'],res.result.status_code)
        self.logger.info("login res {0}".format(res))

class casedataTreating(BaseDataTreating):
    def customTreating(self,name,value):
        #可以自定义用例数据转换，然后在用例中使用
        #casedataTreating.treating(name,value)方法即可，默认提供全局变量替换
        return value