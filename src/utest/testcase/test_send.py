# coding=utf-8
import time
import unittest
from bear.base import Ski


class TestSendMessage(unittest.TestCase,Ski):

    def setUp(self):
    #    print("I'm in test_two setUP")
        pass
    def tearDown(self):
        pass
        # print("I'm in test_two teardown")

    @Ski.case()
    def test_send(self):
        print("I'm in test_two test_send")
        # print(self.ski_step_result)
        self.assertTrue(True)
        res=self.step("userkw_sendmsg","get","http://www.baidu.com")
        print(res)
        self.assertEqual(200,res.result.status_code)
    
    @Ski.case()
    def test_send_use_robotframework_requestlibary(self):
        print("I'm in test_two test_send")
        # print(self.ski_step_result)
        self.assertTrue(True)
        self.step("Create Session","baidu","http://www.baidu.com")
        res=self.step("Get Request","baidu","/")
        self.assertEqual(200,res.result.status_code)

    @Ski.case()
    def test_robotframwork_selenium(self):
        print("I'm in test_two test_send")
        self.step("Open Browser","http://www.baidu.com","chrome")
        self.step("input text","id=kw","test_robot")
        self.step("click button","id=su")
