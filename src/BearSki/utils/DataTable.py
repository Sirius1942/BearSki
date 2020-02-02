from openpyxl import load_workbook
import time
import re
import random
import logging
import sys
import json


logger=logging.getLogger("BearSki.DataTable")

def getRowData(data="",datafile=""):
  datalist=data.split(".")
  wb = load_workbook(filename = datafile)
  sheet_ranges = wb[datalist[0]]
  values=sheet_ranges.values
  clumtitle=next(values)
  for rowdata in values:
      if rowdata[0]==datalist[1]:
        if len(datalist)==2:
          logger.debug(u"获取数据源原始数据：标题行 [{0}] 数据行 [{1}]".format(clumtitle,rowdata))
          return clumtitle,rowdata
        else:
          try:
            i=clumtitle.index(datalist[2])
          except ValueError:
            raise DataTableError("数据索引异常 [{0}] 中 {1} 数据异常，请检查".format(data,datalist[2]))
          logger.debug(u"获取数据源原始数据：标题 [{0}] 数据 [{1}]".format(clumtitle[i],rowdata[i]))
          return clumtitle[i],rowdata[i]
  raise DataTableError("没有找到需要获取的数据 [{0}] ，请检查数据是否存在，索引是否正确".format(data))


def generate_json_data(title,RowData):
  re={}
  if type(RowData)==type("str"):
    re[title]=sfun(RowData)
    return re
  else:
    re["dataid"]=""
    re["remark"]=""
    re['detail']={}
    for i in range(0,len(RowData)):
      if title[i]=="DataID":
         re["dataid"]=sfun(RowData[i])
      elif title[i]=="Remark":
        re["remark"]=sfun(RowData[i])
      elif title[i]== None:
        continue
      elif RowData[i] ==None:
        re['detail'][title[i]]=""
      else :
        re['detail'][title[i]]=sfun(RowData[i])
    return re

def generate_data(title,RowData):
  if type(RowData)==type("str"):
    return sfun(RowData)
  else:
    re=[]
    for i in range(0,len(RowData)):
      if title[i]=="DataID":
         continue
      elif title[i]=="Remark":
         continue
      elif title[i]== None:
        continue
      elif RowData[i] ==None:
        re.append("")
      else :
        re.append(sfun(RowData[i]))
    return re

# 后续需要修改代码，提升正则速度，减少正则对比次数
def sfun(re_str):
  nstr=s_fun(re_str)
  if nstr == re_str:
    return s_jl_fun(re_str)
  return nstr

def s_fun(re_str):
  pattern = re.compile(r'\$\{.*?\}')
  longstr=pattern.finditer(str(re_str)) ##需要字符串
  result=str(re_str)
  for value in longstr:
    newdata=runfun(value.group())
    result=result.replace(value.group(),newdata,1)
  return result

def s_jl_fun(re_str):
  # print("in sfun")
  pattern = re.compile(r'\$((json)|(list))\{.*?\}')
  longstr=pattern.finditer(str(re_str)) ##需要字符串
  result=str(re_str)
  for value in longstr:
    result=get_jl(value.group())
    # result=result.replace(value.group(),newdata,1)
  return result

def get_jl(cellstr):
  type_str=cellstr[1:5]
  if type_str == "json":
    json_str=cellstr[6:]
    try:
      rejson=json.loads(json_str)
    except json.decoder.JSONDecodeError: 
      raise DataTableError("数据[{0}],转化json 类型异常".format(json_str))
    return rejson
  if type_str == "list":
    list_str=cellstr[6:-1]
    # print(list_str)
    relist=list_str.split(",")
    re=[]
    for svalue in relist:
      if svalue.find('.int') != -1:
        re.append(int(svalue[:-4]))
        continue
      re.append(svalue)
    return re

def runfun(cellstr):
  if cellstr.find('time.now') != -1:
      newvalue=time.strftime("\"%Y-%m-%d %H:%M:%S\"", time.localtime())
      return newvalue
  elif cellstr.find('random.int')!= -1:
      newvalue=getRand_int(int(cellstr[13:-2]))
      return newvalue
  else:
      return cellstr

def getRand_int(num):
  star=10**(num-1)
  end=10**(num)-1
  # V1.2.18 修改随机数位数计算错误问题
  return str(random.randint(star,end))

def getJsonData(filename="",filepath=""):
  fo = open(filepath+filename, "r+",encoding='utf8')
  jstr=sfun(fo.read())
  redata=json.loads(jstr)
  return redata

class DataTableError(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)