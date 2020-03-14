# -*- encoding: utf-8 -*-
'''
@File    :   hartool.py
@Time    :   2020/01/29 15:29:32
@Author  :   chenjiusi 
'''
import logging
import json,os
from  har2case.core import HarParser
from BearSki.utils.arguments import runArg 
from BearSki.template import ApiTest_har
logger=logging.getLogger("BearSki.HarTool")
class HarTool(HarParser):
  
    def __init__(self, har_file_path, filter_str=None, exclude_str=None):
        self.har_file_path = har_file_path
        self.filter_str = filter_str
        self.exclude_str = exclude_str or ""
        self._openfiles()
        self.rArg=runArg()

    # 生成单接口测试模型,_prepare_teststep继承harparser方法
    def _getOneRequest(self,entry_json):
        return self._prepare_teststep(entry_json)
        
    def _openfiles(self):
      fo = open(self.har_file_path, "r+",encoding='utf8')
      jstr=json.loads(fo.read())
      req_list=jstr['log']['entries']
      i=0
      self.harfile={}
      for req_index in req_list:
        request_str=self._getOneRequest(req_index)
        name=request_str['name']
        response_str=self._getResponse(req_index)
        self.harfile[name]={}
        self.harfile[name]['request']=request_str
        self.harfile[name]['response']=response_str
    
    def _getResponse(self,req):
    #   print(req)
      return req['response']

    def createAllCase(self):
        for name in self.harfile:
            result,res=self.getMessage(name)
            self.createTestCase(result,res)
    #功能函数
    def getMessage(self,name):
        print(name)
        req=self.harfile[name]['request']
        res=self.harfile[name]['response']
        return req,res
    
    def createOneCase(self,name):
        req=self.harfile[name]['request']
        res=self.harfile[name]['response']
        self.createTestCase(req,res)
    
    def createTestCase(self,req_str,res):
        # print(req_str)
        newrul=req_str['name']
        # print(req_str)
        modelpath=self.rArg.auto_model_path
        casepath=self.rArg.auto_case_path
        modelname=newrul.replace('/','_')[1:-1]
        isExists=os.path.exists(modelpath)
        if not isExists:
          os.makedirs(modelpath)
        self.writeFile(modelpath+'/'+modelname+'_model.json',json.dumps(req_str, sort_keys=True, indent=4, separators=(',', ': '),ensure_ascii=False))
        self.writeFile(modelpath+'/'+modelname+'_res.json',json.dumps(res, sort_keys=True, indent=4, separators=(',', ': '),ensure_ascii=False))

        testcase=ApiTest_har.TESTCASE
        newcase=testcase.replace("${modelname}",modelname).replace("${model_file_path}",modelpath)
        
        self.writeFile(casepath+'/'+"test_auto_"+modelname+'.py',newcase)

    def writeFile(self,filename,context):
        fo= open(filename,"w+")
        # print(context)
        fo.write(context)
        fo.close
      
