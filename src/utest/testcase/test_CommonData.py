from BearSki.CommonData import SkiGlobalData
# coding=utf-8
import time
import unittest
from BearSki.utils.logger import SkiLogger


class TestGloablData(unittest.TestCase):
    def __init__():
        self.logger=SkiLogger("TestGloablData")
    def test_getDefult_data(self):
        self.logger.info("I'm in test_getDefult_data")
        BASE_URL=SkiGlobalData().get_global_data("BASE_URL")
        self.assertEqual(BASE_URL,"http://www.baidu.com")
    def test_setGlobalData(self):
        self.logger.info("I'm in test_getDefult_data")
        SkiGlobalData().add_global_data({"A1":"d1","A2":456})
        A1=SkiGlobalData().get_global_all_data()["A1"]
        A2=SkiGlobalData().get_global_all_data()["A2"]
        self.assertEqual(A1,"d1")
        self.assertEqual(A2,456)
        