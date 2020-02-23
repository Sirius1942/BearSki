#!/usr/bin/python3
import json
import requests

# 读取消息文件
fo = open("h13.har", "r+",encoding='utf8')
jstr=json.loads(fo.read())
request_str=jstr['log']['entries'][0]['request']
postdata=jstr['log']['entries'][0]['request']['postData']['text']
respone_str=jstr['log']['entries'][0]['response']
headers_list=request_str['headers']
headers_dic={}
for hvalue in headers_list:
  headers_dic[hvalue['name']]=hvalue['value']

# print("har 文件中的请求内容: {0}".format(request_str))
# print("har 文件中的消息返回值: {0}".format(respone_str))
# harDirct = json.loads(fo.read())
print("postdata is {0}".format(postdata))
print("postdata type is {0}".format(type(postdata)))
print("postdata change is {0}".format(type(json.dumps(postdata))))
#根据har 文件中的内容发送新的请求
res=requests.post(request_str['url'],headers=headers_dic,json=json.loads(postdata))

#requests的返回值
print("根据har文件发送请求的返回值： {0}".format(res.text))
# 关闭文件

fo.close()