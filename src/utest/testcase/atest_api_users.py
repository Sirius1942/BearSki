
# coding=utf-8
import time
import unittest
from BearSki.core import Ski
from BearSki.core import DT
import logging
import json
from BearSki.core import DT

class test_api_users(unittest.TestCase,Ski):

    def setUp(self):
        self.logger=logging.getLogger("test_api_users")
    def tearDown(self):
        pass
    @Ski.case()
    def case_api_users(self):
        model_name="api_users"
        self.logger.info("in case_api_users")
        mjstr=DT.json(model_name+'_model.json')
        res=self.step("requestFromModel",mjstr)
        jstr=DT.json(model_name+"_res.json")
        self.assertEqual(jstr['status'],res.result.status_code)
        self.logger.info("login res {0}".format(res))
