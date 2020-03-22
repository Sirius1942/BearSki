from abc import ABCMeta, abstractmethod
import threading
import random
import pytest
import logging
import unittest
import time
from BearSki.runner.LocalReportRunner import LocalReportRunner
from BearSki.core import Ski
loggger=logging.getLogger("BearSki.TestSuitSet")

class TestSuit(metaclass=ABCMeta):
    def __init__(self,runArg,commond):
        self.commond = commond
        self.runArg=runArg
        self.caselist=[]
        self.createSuit()
    @ abstractmethod
    def createSuit(self):
        pass
    def getCommond(self):
        return self.commond
    def getRunArg(self):
        return self.runArg.getJsonString()
    def addcaselist(self,caselist):
        self.caselist=caselist
    @abstractmethod
    def runTest(self):
        pass

class UnitTestRunner(TestSuit):

    def createSuit(self):
        isrunonecase = False
        if self.runArg.mode == 'onecase':
            isrunonecase = True
        casepath = self.runArg.case_path
        casename = self.runArg.case_name
        caselist = self._get_test_cases(casepath, casename, isrunonecase)
        self.addcaselist(caselist)

    def _get_test_cases(self, dirpath, name="test_", isrunonecase=False):
        test_cases = unittest.TestSuite()
        # 测试用例使用"ski_"开头命名
        if isrunonecase:
            # 执行单条用例，顺序为 目录名 文件名 类名 方法名 中间"." 间隔 例如："testcase.debug_test_user.TestUserLogin.test_login"
            suite = unittest.TestLoader().loadTestsFromName(dirpath)
            test_cases.addTests(suite)
            return test_cases
        else:
            suites = unittest.defaultTestLoader.discover(dirpath, name + '*.py', top_level_dir=dirpath)
            for suite in suites:
                test_cases.addTests(suite)
            return test_cases

    @Ski.init()
    def runTest(self):
        if (self.runArg.report_mode == 'text'):
            # self.logger.info("开始执行测试,报告输出模式text")
            runner = unittest.TextTestRunner()
            runner.run(self.caselist)
        elif (self.runArg.report_mode == 'html'):
            # self.logger.info("开始执行测试,报告输出模式html")
            lruner = LocalReportRunner()
            lruner.run(self.caselist)
            # self.logger.info("测试完成,报告输出模式html")

class PyTestRunner(TestSuit):
    def createSuit(self):
        pass
    def runTest(self):
        pytest.main(self.commond)

