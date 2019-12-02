# -*- encoding: utf-8 -*-
'''
@File    :   CommandLine.py
@Time    :   2019/11/20 11:28:10
@Author  :   Sirius 
'''
import sys, getopt
import json
import os
from BearSki.utils.command import command_parser
from BearSki.utils.command import base_command
from BearSki.utils.arguments import runArg
from BearSki.utils.errors import ArgmentError
from BearSki.RunUnittest import RunUnittest
from BearSki.utils.logger import LoggerBaseConfig
import logging 

class CommandLine(object):
    command_list=[
        ["h","help","show help"],
        ["m","mode","run all test or oncase"],
        ["f","configfile","config path"],
        ["p","casepath","run casepath"],
        ["n","casename","run casename"],
        ["r","reportmode","test report ouput mode"],
        ["o","outputpath","test report ouput path"],
        ["j","jsonfile","json file path"]
      ]# 短命令超过1个字符 getopt会出错，暂时遗留问题
    cps=command_parser()
    rarg=runArg()
    def __init__(self,argv):
      # LoggerBaseConfig()._initlogger()
      self.logger=logging.getLogger("BearSki.commondline")
      for cmd in self.command_list:
        help_cmd=base_command(cmd[0],cmd[1],cmd[2])
        self.cps.add_argument(help_cmd)
      self._run(argv)
      
    def _run(self,argv):
      shot_cmd = self.cps.get_shot_arg()
      long_cmd = self.cps.get_long_arg()
      arguments=argv[1:]
      if len(arguments)<2:
        arguments.append(" ") # 命令行参数为空
      try:
          opts, args = getopt.getopt(arguments,shot_cmd,long_cmd)
      except getopt.GetoptError as e:
          # print (e)
          self.logger.error(e)
          sys.exit(2)
      for opt, arg in opts:
          if opt in ('-h',"--help"):
            self._command_h()
            sys.exit()
          elif opt in ("-f", "--configfile"):
            self.rarg.config_path=arg.lstrip() #.lstrip() 去掉多余的空格
            self._command_f(arg.lstrip())
            break
          elif opt in ("-r","--reportmode"):
            self.rarg.report_mode = arg.lstrip()
          elif opt in ("-m","--mode"):
            self.rarg.mode = arg.lstrip()
          elif opt in ("-p","--casepath"):
            self.rarg.case_path=arg.lstrip()
          elif opt in ("-n","--casename"):
            self.rarg.case_name = arg.lstrip()
          elif opt in ("-o","--outputpath"):
            self.rarg.report_path = arg.lstrip()
      self._command_run(self.rarg)
    
    def _command_h(self):
      self.cps.print_help_message()
          
    def _command_f(self,filepath):
       f= open(filepath)
       conf=json.load(f)
       self.rarg.setValueFromJson(conf)
      #  print(self.rarg.getJsonString())

    def _command_run(self,argObject):
      RunUnittest().runTest(argObject)
    
    

    
    
    



      
  