# -*- encoding: utf-8 -*-
'''
@File    :   DataTreating.py
@Time    :   2020/02/02 16:10:07
@Author  :   chenjiusi 
'''
from BearSki.CommonData import SkiGlobalData

class BaseDataTreating(object):

  def __init__(self):
    self.sgd=SkiGlobalData()

  def treating(self,name,value):
    #先进行全局变量替换，再进行自定义方法替换
    revalue=self.treatingGlobalData(name,value)
    revalue=self.customTreating(name,revalue)
    return revalue

  def treatingGlobalData(self,name,value):
    revalue=SkiGlobalData().get_global_data(name)
    if revalue==None:
      return value
    else:
      return revalue

  def customTreating(self,name,value):
    return value
    ##全局替换，接口基本替换，用例替换，自定义替换 自定义数据处理