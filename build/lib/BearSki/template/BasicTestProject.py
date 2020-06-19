import os
import logging
from  BearSki.template.CreateDataTableFile import createDTF 
DRIVER_NAME='d_requests.py'
DRIVER_DOC='''
import requests
def get(url, params=None, **kwargs):
  return requests.get(url,params,**kwargs)

def post(url, data=None, json=None, **kwargs):
  return requests.post(url, data, json, **kwargs)

def delete(url, **kwargs):
  return requests.delete(url, **kwargs)

def put(url, data=None, **kwargs):
  return requests.put(url, data=None, **kwargs)

def patch(url, data=None, **kwargs):
  return requests.patch(url, data=None, **kwargs)

def head(url, **kwargs):
  return requests.head(url, **kwargs)

def options(url, **kwargs):
  return requests.options(url,**kwargs)
'''
KEYWORD_NAME='send.py'
KEYWORD_DOC='''
from driver import d_requests
from BearSki.utils.logger import SkiLogger

logger=SkiLogger('keywords.send')

def askbaidu(mod,data):
    logger.info('in ask baidu！')
    r = d_requests.get(url=data)
    return r
'''
TESTCASE_NAME='test_send.py'
TESTCASE_DOC='''
# coding=utf-8
import time
import unittest
from BearSki.core import Ski,TD
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
    def test_columns_data(self):
        self.logger.info("in test_columns_data ")
        data=TD.get_columns_data("example.DataID")
        self.logger.info(data)
        self.logger.info("in test_getData")
        name=TD.get_Data("example.admin.username")
        self.assertEqual(name['username'],"admin")
        admindata = TD.get_Data("example.admin")
        self.assertEqual(admindata['detail']['username'], "admin")
    
    # @Ski.case()
    # def test_send_use_robotframework_requestlibary(self):
    #     self.logger.info("I'm in test_two test_send")
    #     # print(self.ski_step_result)
    #     # self.assertTrue(True)
    #     self.step("Create Session","baidu","http://www.baidu.com")
    #     res=self.step("Get Request","baidu","/")
    #     self.assertEqual(200,res.result.status_code)

    # @Ski.case()
    # def test_robotframwork_selenium(self):
    #     self.logger.info("I'm in test_two test_send")
    #     self.step("Open Browser","http://www.baidu.com","chrome")
    #     self.step("input text","id=kw","test_robot") 
    #     self.step("click button","id=su")
'''
CONFIG_NAME='config.yaml'
CONFIG_DOC='''
runner:
  name: PyTestRunner
  commands:
    - -s
unittestcase:
  mode: onecase
case:
  path: testcase.atest_api_users.atest_api_users.case_api_users
  name: ""
ski_filepath: SkiSetting.py
report:
  mode: html
  path: report/report1.html
  addtime.now: true
auto:
  case_path: testdata/model
  model_path": testdata/model
log:
  file_path: log/log.log
  level: INFO
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
SKISETTING_NAME='SkiSetting.py'
SKISETTING_DOC='''
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

KW_ROUTER={
        "userkw_sendmsg":"keywords.send.askbaidu",
        "Create Session":"RequestsLibrary.RequestsLibrary.create_session",
        "Get Request":"RequestsLibrary.RequestsLibrary.get_request",
        "input text":"Selenium2Library.Selenium2Library.input_text",
        "click button":"Selenium2Library.Selenium2Library.click_button",
        "Open Browser":"Selenium2Library.Selenium2Library.open_browser",
        "requestFromModel":"keywords.requestModel.runModel"
}
GLOBAL_VARIABLE={
        "BASE_URL":"http://www.agavetest.cn:8671",
    }
DATATABLE={
        "db_excel_path":"testdata/testdata1.xlsx",
        "db_json_path":"testdata/model/"
    }

TEST_DATABASES = {
    'default': {
        'ENGINE': 'BearSki.db.Base.ExcelFile',
        'NAME': 'myDataTable', #连接的数据库名
        'PATH': 'testdata/testdata.xlsx'
    },
    'myJsonData': {
        'ENGINE': 'Bearski.db.Base.JsonFile',
        'NAME': 'myJsonData', #连接的数据库名
        'PATH': 'testdata/model/'
    }
}
#TEST_DATABASE_ROUTERS = ['myproject.database_router.DatabaseAppsRouter']
TEST_DAT_AUTOMAPPING=True

TEST_DATABASE_CASE_MAPPING = {
    'app01': 'default',
    'app02': 'mysql02',
}
INITDATA={
        "init_file_path":"testdata.initdata"
}

'''
INITDATAFILE='''
def initData():
    print("in initData")
def clear():
    print("in initData clear")
'''
INITDATANAME='initdata.py'
INITFILE='__init__.py'
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

    initfile=os.path.join(projectname,'testdata')
    os.makedirs(initfile)

    driverf = os.path.join(drd,DRIVER_NAME)
    df=open(driverf, "w+")
    df.write(DRIVER_DOC)
    df.close

    driverf_init = os.path.join(drd, INITFILE)
    dfi = open(driverf_init, "w+")
    dfi.write("")
    dfi.close

    keywordf=os.path.join(kwd,KEYWORD_NAME)
    kf=open(keywordf, "w+")
    kf.write(KEYWORD_DOC)
    kf.close

    testcasef=os.path.join(tcd,TESTCASE_NAME)
    tf=open(testcasef, "w+")
    tf.write(TESTCASE_DOC)
    tf.close

    initdf=os.path.join(initfile,INITDATANAME)
    idf=open(initdf, "w+")
    idf.write(INITDATAFILE)
    idf.close

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

    try:
        createDTF(initfile)
    except Exception as e:
        logger.error(e)
        logger.error('创建excel 数据表样例失败')

    logger.info('测试项目创建完成')


     
      

  
    

