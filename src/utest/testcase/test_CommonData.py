from BearSki.CommonData import SkiGlobalData
# coding=utf-8
import time
import unittest

class TestGloablData(unittest.TestCase):
    def test_getDefult_data(self):
        print("I'm in test_getDefult_data")
        BASE_URL=SkiGlobalData().get_global_data("BASE_URL")
        self.assertEqual(BASE_URL,"http://www.baidu.com")
    def test_setGlobalData(self):
        print("I'm in test_getDefult_data")
        SkiGlobalData().add_global_data({"A1":"d1","A2":456})
        A1=SkiGlobalData().get_global_all_data()["A1"]
        A2=SkiGlobalData().get_global_all_data()["A2"]
        self.assertEqual(A1,"d1")
        self.assertEqual(A2,456)
        