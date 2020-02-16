TESTCASE='''
# coding=utf-8
import time
import unittest
from BearSki.core import Ski
from BearSki.core import DT
import logging
import json

class atest_${modelname}(unittest.TestCase,Ski):

    def setUp(self):
        self.logger=logging.getLogger("atest_${modelname}")
    def tearDown(self):
        pass
    @Ski.case()
    def case_${modelname}(self):
        model_name="${modelname}"
        self.logger.info("in case_${modelname}")
        mjstr=DT.json(model_name+'_model.json')
        res=self.step("requestFromModel",mjstr)
        jstr=DT.json(model_name+"_res.json")
        self.assertEqual(jstr['status'],res.result.status_code)
        self.logger.info("login res {0}".format(res))
'''
