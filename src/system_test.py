# -*- encoding: utf-8 -*-
#BearSki 测试类
'''
@File    :   test.py
@Time    :   2020/01/30 23:29:00
@Author  :   chenjiusi 
'''

# coding=utf-8
import time
import unittest
from  BearSki import *
import json
import subprocess
from unittest import mock
from BearSki.utils.logger import SkiLogger
import os
import multiprocessing



logger=SkiLogger("test")
class test_BearSki(unittest.TestCase):
    ASSREQ ="/auth/login/"
    ASSRES={
    "_transferSize": 419,
    "bodySize": 234,
    "content": {
        "compression": 0,
        "mimeType": "application/json",
        "size": 234,
        "text": "{\"code\":200,\"message\":\"成功\",\"detail\":{\"token\":\"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTc5OTQ0MjYyLCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.J55Jx9dvfIrILZMRnnYzIeJjM9EUkbU6ekS3I6qJH8M\"}}"
    },
    "cookies": [],
    "headers": [
        {
            "name": "Content-Type",
            "value": "application/json"
        },
        {
            "name": "Vary",
            "value": "Accept, Cookie, Origin"
        },
        {
            "name": "Allow",
            "value": "POST, OPTIONS"
        },
        {
            "name": "X-Frame-Options",
            "value": "SAMEORIGIN"
        },
        {
            "name": "Content-Length",
            "value": "234"
        },
        {
            "name": "Access-Control-Allow-Origin",
            "value": "*"
        }
    ],
    "headersSize": 185,
    "httpVersion": "HTTP/1.1",
    "redirectURL": "",
    "status": 200,
    "statusText": "OK"
}     
    HARFILE ={
  "log": {
    "version": "1.2",
    "creator": {
      "name": "WebInspector",
      "version": "537.36"
    },
    "pages": [],
    "entries": [
      {
        "startedDateTime": "2020-01-22T09:24:22.067Z",
        "time": 383.9049999951385,
        "request": {
          "method": "POST",
          "url": "http://localhost.charlesproxy.com:8086/auth/login/",
          "httpVersion": "HTTP/1.1",
          "headers": [
            {
              "name": "Host",
              "value": "localhost.charlesproxy.com:8086"
            },
            {
              "name": "Connection",
              "value": "keep-alive"
            },
            {
              "name": "Content-Length",
              "value": "48"
            },
            {
              "name": "Accept",
              "value": "application/json, text/plain, */*"
            },
            {
              "name": "Origin",
              "value": "http://localhost:9527"
            },
            {
              "name": "User-Agent",
              "value": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
            },
            {
              "name": "Content-Type",
              "value": "application/json;charset=UTF-8"
            },
            {
              "name": "Accept-Language",
              "value": "zh-CN,zh;q=0.9"
            }
          ],
          "queryString": [],
          "cookies": [],
          "headersSize": 464,
          "bodySize": 48,
          "postData": {
            "mimeType": "application/json;charset=UTF-8",
            "text": "{\"username\":\"admin\",\"password\":\"AgaveTest@5567\"}"
          }
        },
        "response": {
          "status": 200,
          "statusText": "OK",
          "httpVersion": "HTTP/1.1",
          "headers": [
            {
              "name": "Content-Type",
              "value": "application/json"
            },
            {
              "name": "Vary",
              "value": "Accept, Cookie, Origin"
            },
            {
              "name": "Allow",
              "value": "POST, OPTIONS"
            },
            {
              "name": "X-Frame-Options",
              "value": "SAMEORIGIN"
            },
            {
              "name": "Content-Length",
              "value": "234"
            },
            {
              "name": "Access-Control-Allow-Origin",
              "value": "*"
            }
          ],
          "cookies": [],
          "content": {
            "size": 234,
            "mimeType": "application/json",
            "compression": 0,
            "text": "{\"code\":200,\"message\":\"成功\",\"detail\":{\"token\":\"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTc5OTQ0MjYyLCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.J55Jx9dvfIrILZMRnnYzIeJjM9EUkbU6ekS3I6qJH8M\"}}"
          },
          "redirectURL": "",
          "headersSize": 185,
          "bodySize": 234,
          "_transferSize": 419
        },
        "cache": {},
        "timings": {
          "blocked": 4.479999983806163,
          "dns": -1,
          "ssl": -1,
          "connect": -1,
          "send": 0.12200000000000011,
          "wait": 378.64500000685456,
          "receive": 0.6580000044777989,
          "_blocked_queueing": 3.261999983806163
        },
        "serverIPAddress": "127.0.0.1",
        "_initiator": {
          "type": "script",
          "stack": {
            "callFrames": [
              {
                "functionName": "dispatchXhrRequest",
                "scriptId": "5",
                "url": "http://localhost:9527/app.js",
                "lineNumber": 26472,
                "columnNumber": 12
              },
              {
                "functionName": "xhrAdapter",
                "scriptId": "5",
                "url": "http://localhost:9527/app.js",
                "lineNumber": 26306,
                "columnNumber": 9
              },
              {
                "functionName": "dispatchRequest",
                "scriptId": "5",
                "url": "http://localhost:9527/app.js",
                "lineNumber": 26952,
                "columnNumber": 9
              }
            ],
            "parent": {
              "description": "Promise.then",
              "callFrames": [
                {
                  "functionName": "request",
                  "scriptId": "5",
                  "url": "http://localhost:9527/app.js",
                  "lineNumber": 26729,
                  "columnNumber": 22
                },
                {
                  "functionName": "wrap",
                  "scriptId": "5",
                  "url": "http://localhost:9527/app.js",
                  "lineNumber": 27318,
                  "columnNumber": 14
                },
                {
                  "functionName": "login",
                  "scriptId": "5",
                  "url": "http://localhost:9527/app.js",
                  "lineNumber": 411398,
                  "columnNumber": 30
                }
              ]
            }
          }
        },
        "_priority": "High",
        "_resourceType": "xhr",
        "connection": "491626"
      }
    ]
  }
}
    @classmethod
    def setUpClass(cls):
        # 所有case的前置条件
        subprocess.run(['python','runcmd.py','createproject','-n','AgaveTestProject'])
        
    @classmethod
    def tearDownClass(cls):
        # 所有case的后置条件
        subprocess.run(['rm','-rf','AgaveTestProject'])
        # logger.info('清除测试项目')
        pass
        
    def setUp(self):
        # 每条case的前置条件
        pass
    def tearDown(self):
        #这是每条case的后置条件
        pass
    def testBearCLI_1(self): 
        result = subprocess.run(['python','runcmd.py','-h'],stderr=subprocess.PIPE,stdout=subprocess.PIPE)
        # result = subprocess.run(['python','test1.py','-v'],stderr=subprocess.PIPE,stdout=subprocess.PIPE,check=True)
        # 非正常终止时候如果check=True 将不会输入出错误信息，仅提示错误
        # 测试命令行代码帮助信息
        self.assertIn('createproject', str(result.stdout))
        # logger.info(result.stdout)

    def testBearCLI_2(self): 
        result = subprocess.run(['python','runcmd.py','tools','-gt'],stderr=subprocess.PIPE,stdout=subprocess.PIPE)
        self.assertIn('guitools startup', str(result.stdout))
        logger.info(result.stdout)

    def testBearCLI_4(self): 
        i=0
        while (i<10):
          isExists=os.path.exists('AgaveTestProject')
          if not isExists:
            time.sleep(1)
            i+=1
          else:
            break
        # os.system("cd AgaveTestProject && python runtest.py")
        
        # r = os.popen("cd AgaveTestProject && python runtest.py")  
        # text = r.read()  
        # r.close() 
        result = subprocess.run(['sh','run_stest.sh'],stderr=subprocess.PIPE,stdout=subprocess.PIPE)
        logger.info(result.stdout)
        # print("test is :",text)
        #临时加的判断
        self.assertIn('initData clear', str(result.stdout))

    @unittest.skip('不执行case:') # 跳过这条case
    def testskipcase(self): 
        print('这是被跳过不执行的用例')
    
if __name__=='__main__':

    report_type=input("run alltest ?(y or n):")
    if report_type== "y":
        unittest.main()
    else:
        suite = unittest.TestSuite()
        suite.addTest(test_BearSki('testBearCLI_4'))
        unittest.TextTestRunner().run(suite)