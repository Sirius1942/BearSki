
    
# coding=utf-8
import time
import unittest
from BearSki.base import Ski
from BearSki.base import DT
import logging
import json

class test__api_roles(unittest.TestCase,Ski):

    def setUp(self):
        self.logger=logging.getLogger("test__api_roles")
    def tearDown(self):
        pass
    @Ski.case()
    def case__api_roles(self):
        model_name="_api_roles"
        self.logger.info("in case__api_roles")
        res=self.step("requestFromModel",model_name+'_model.json')
        fo = open("../testdata/model/"+model_name+"_rep.json", "r+",encoding='utf8')
        jstr=json.loads(fo.read())
        self.assertEqual(jstr['status'],res.result.status_code)
        self.logger.info("login res {0}".format(res))
