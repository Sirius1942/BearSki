from abc import ABCMeta, abstractmethod
import threading
import random

class TestSuit(metaclass=ABCMeta):
    def __init__(self,caselist):
        self.testcaselist = []
        self.createSuit(caselist)
    @ abstractmethod
    def createSuit(self):
        pass
    def getCaselist(self):
        return self.testcaselist
    def addCaselist(self, caselist):
        self.testcaselist=caselist
    @abstractmethod
    def run(self):
        pass

class SequentialTestRunner(TestSuit):
    def createSuit(self,caselist):
        self.addCaselist(caselist)
    def run(self):
        for testcase in self.getCaselist():
            print(testcase.run().getResult())

class ParallelTestRunner(TestSuit):

    def createSuit(self, caselist):
        self.addCaselist(caselist)
    def run(self):
        for testcase in self.getCaselist():
            self.TestSuitThread(testcase).start()

    class TestSuitThread(threading.Thread):
        def __init__(self, TestCase):
            threading.Thread.__init__(self)
            self.testcase = TestCase
        def run(self):
            result=self.testcase.run().getResult()
            print("开启用例执行线程,结果： {0}".format(result))
            return result

class RandomTestRunner(TestSuit):
    def createSuit(self, caselist):
        self.addCaselist(caselist)
    def run(self):
        number=random.randint(0,len(self.getCaselist())-1)
        print("radom number is :{0}".format(number))
        print(self.getCaselist()[number].run().getResult())