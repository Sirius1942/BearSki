# coding=utf-8
import time
import unittest
from BearSki.base import Ski
from BearSki.base import DT
import logging




class TestDataTable(unittest.TestCase,Ski):

    def setUp(self):
        self.logger=logging.getLogger('TestDataTable')
        
    def tearDown(self):
        pass

    @Ski.case()
    def test_datatable(self):
        self.logger.info("I'm in test_datatable")
        data1=DT("users.admin").list()
        self.logger.info(DT("users.admin.time").list())
        self.logger.info(DT("users.admin").json())
        self.logger.info(DT("users.admin.time").json())
        # print(self.ski_step_result)
        # self.assertTrue(True)
        # res=self.step("userkw_sendmsg","get","http://www.baidu.com")
        # self.logger.info(res.result)
        # self.assertEqual(200,res.result.status_code)
    
   