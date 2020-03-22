from abc import ABCMeta, abstractmethod

class TestResult(metaclass = ABCMeta):
    @abstractmethod
    def getResult(self):
        return object

class SkiTestResult(TestResult):
    result={}
    def __init__(self,result,message):
        self.result["result"]=result
        self.result["message"]=message

    def getResult(self):
        return self.result