from abc import ABCMeta, abstractmethod
import time
from BearSki.case.TestResultSet import *
class TestCase(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        return TestResult()

class SkiTestCase(TestCase):
    def run(self):
        tmuber=time.ctime(time.time())
        time.sleep(1) #模拟用例执行时间
        return SkiTestResult(True,"Skitestcase was run! start time is :{0}".format(tmuber))

class unnitTestCase(TestCase):
    def run(self):
        tmuber = time.ctime(time.time())
        time.sleep(1)  # 模拟用例执行时间
        return SkiTestResult(True, "unnitTestCase was run! start time is :{0}".format(tmuber))