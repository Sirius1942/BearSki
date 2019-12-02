# coding=utf-8
import time
import unittest
from BearSki.base import Ski
from BearSki.utils.logger import SkiLogger



class TestSendMessage(unittest.TestCase,Ski):

    def setUp(self):
        self.logger=SkiLogger('TestSendMessage')
        
    def tearDown(self):
        pass

    @Ski.case()
    def test_send(self):
        self.logger.info("I'm in test_two test_send")
        # print(self.ski_step_result)
        self.assertTrue(True)
        res=self.step("userkw_sendmsg","get","http://www.baidu.com")
        self.logger.info(res.result)
        self.assertEqual(200,res.result.status_code)
    
    @Ski.case()
    def test_send_use_robotframework_requestlibary(self):
        self.logger.info("I'm in test_two test_send")
        # print(self.ski_step_result)
        # self.assertTrue(True)
        self.step("Create Session","baidu","http://www.baidu.com")
        res=self.step("Get Request","baidu","/")
        self.assertEqual(200,res.result.status_code)

    # @Ski.case()
    # def test_robotframwork_selenium(self):
    #     self.logger.info("I'm in test_two test_send")
    #     self.step("Open Browser","http://www.baidu.com","chrome")
    #     self.step("input text","id=kw","test_robot")
    #     self.step("click button","id=su")
