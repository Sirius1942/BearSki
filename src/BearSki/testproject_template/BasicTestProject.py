import os
import logging
DRIVER_NAME='d_requests.py'
DRIVER_DOC='''
import requests

def get(url, params=None, **kwargs):
  return requests.get(url,params,**kwargs)

def post(url, data=None, json=None, **kwargs):
  return requests.post(url, data, json, **kwargs)
'''
KEYWORD_NAME='send.py'
KEYWORD_DOC='''
from driver import d_requests
from BearSki.utils.logger import SkiLogger

logger=SkiLogger('keywords.send')

def askbaidu(mod,data):
    logger.info('in ask baidu！')
    r = d_requests.get(url=data)    # 最基本的GET请求
    return r
'''
TESTCASE_NAME='test_send.py'
TESTCASE_DOC='''
# coding=utf-8
import time
import unittest
from BearSki.base import Ski
import logging
class TestSendMessage(unittest.TestCase,Ski):
    def setUp(self):
        self.logger=logging.getLogger('TestSendMessage')
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
'''
CONFIG_NAME='config.json'
CONFIG_DOC='''
{
    "m":"allcase",
    "p":"./testcase",
    "n":"",
    "r":"html",
    "o":"./report/result.html",
    "j":"./SkiSetting.json"
}
'''
RUNTEST_NAME='runtest.py'
RUNTEST_DOC='''
import sys

if __name__ == '__main__':
    try:
        from BearSki.CommandLine import CommandLine 
    except ImportError as exc:
        raise ImportError(
            "Couldn't import BearSki. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    CommandLine(sys.argv)
'''
SKISETTING_NAME='SkiSetting.json'
SKISETTING_DOC='''
{
    "routers":{
        "userkw_sendmsg":"keywords.send.askbaidu",
        "Create Session":"RequestsLibrary.RequestsLibrary.create_session",
        "Get Request":"RequestsLibrary.RequestsLibrary.get_request",
        "input text":"Selenium2Library.Selenium2Library.input_text",
        "click button":"Selenium2Library.Selenium2Library.click_button",
        "Open Browser":"Selenium2Library.Selenium2Library.open_browser"
    },
    "global_variable":{
        "BASE_URL":"http://www.baidu.com",
        "logfile_path":"./log/log.log",
        "log_level":"debug"
    }
    
}
'''

def create_testproject(projectname):
    # (logfile_path, logfile_name) = os.path.split(config_json)
    # if projectname and logfile_name:
    isExists=os.path.exists(projectname)
    if not isExists:
      os.makedirs(projectname)
    logger=logging.getLogger('BearSki.createproject')
    logger.info('开始创建测试项目')
    drd=os.path.join(projectname,'driver')
    os.makedirs(drd)
    kwd=os.path.join(projectname,'keywords')
    os.makedirs(kwd)
    tcd=os.path.join(projectname,'testcase')
    os.makedirs(tcd)
    red=os.path.join(projectname,'report')
    os.makedirs(red)

    driverf = os.path.join(drd,DRIVER_NAME)
    df=open(driverf, "w+")
    df.write(DRIVER_DOC)
    df.close

    keywordf=os.path.join(kwd,KEYWORD_NAME)
    kf=open(keywordf, "w+")
    kf.write(KEYWORD_DOC)
    kf.close

    testcasef=os.path.join(tcd,TESTCASE_NAME)
    tf=open(testcasef, "w+")
    tf.write(TESTCASE_DOC)
    tf.close

    configf=os.path.join(projectname,CONFIG_NAME)
    cf=open(configf, "w+")
    cf.write(CONFIG_DOC)
    cf.close

    skisettingf=os.path.join(projectname,SKISETTING_NAME)
    sf=open(skisettingf, "w+")
    sf.write(SKISETTING_DOC)
    sf.close

    runtestf=os.path.join(projectname,RUNTEST_NAME)
    rf=open(runtestf, "w+")
    rf.write(RUNTEST_DOC)
    rf.close

    logger.info('测试项目创建完成')


     
      

  
    

