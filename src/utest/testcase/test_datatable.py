# coding=utf-8
import time
import unittest
from BearSki.core import Ski
from BearSki.core import DT
import logging

class TestDataTable(unittest.TestCase,Ski):

    def setUp(self):
        self.logger=logging.getLogger('TestDataTable')
        
    def tearDown(self):
        pass
    @Ski.case()
    def test_datatable(self):
        self.logger.info("I'm in test_datatable")
        data1=DT.excel("users.admin",type="list")
        self.logger.info(DT.excel("users.admin.time",type="list"))
        self.logger.info(DT.excel("users.admin"))
        self.logger.info(DT.excel("users.admin.time"))
        self.logger.info(DT.json("auth_login_res.json"))
    