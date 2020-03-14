
# coding=utf-8
import time
import unittest
from BearSki.core import Ski
from BearSki.core import DT
import logging
import json

class atest_api_users_11(unittest.TestCase,Ski):

    def setUp(self):
        self.logger=logging.getLogger("atest_api_users_11")
    def tearDown(self):
        pass
    @Ski.case()
    def case_api_users_11(self):
        model_name="api_users_11"
        self.logger.info("in case_api_users_11")
        mjstr=DT.json(model_name+'_model.json')
        res=self.step("requestFromModel",mjstr)
        jstr=DT.json(model_name+"_res.json")
        self.assertEqual(jstr['status'],res.result.status_code)
        self.logger.info("login res {0}".format(res))
