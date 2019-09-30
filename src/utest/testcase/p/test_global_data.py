# coding=utf-8
import time
import unittest
from bear.base import Ski
from bear.SkiCommonData import SkiGlobalData
class TestGlobalData(unittest.TestCase,Ski):

    def setUp(self):
    #    print("I'm in test_two setUP")
        pass
    def tearDown(self):
        pass
        # print("I'm in test_two teardown")

    @Ski.case()
    def test_global_data(self):
        testdata={'level1':'level2','list1':{'name':'tom'}}
        sgd=SkiGlobalData()
        self.assertEqual('http://www.baidu.com',sgd.get_global_data()['BASE_URL'])
        sgd.add_global_data(testdata)
        self.assertEqual(testdata['level1'],sgd.get_global_data()['level1'])
        self.assertEqual(testdata['list1'],sgd.get_global_data()['list1'])
    
