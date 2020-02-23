from BearSki.core import Ski
# 测试用例执行方法
def run(jsondata):
  steps=jsondata["steps"]
  print(steps)
  for step in steps:
    #调用BearSki测试步骤执行方法。注意这里需要根据 SkiSetting.json 找到对应关键字
    res=Ski().step(step["keywords"],step["datas"])
  return True
  
if __name__ == '__main__':

  #模拟接收到网页发送的测试步骤
  jsondata={"steps":[
    {"keywords":"userkw_sendmsg","datas":["get","http://www.baidu.com"]},{"keywords":"userkw_sendmsg","datas":["get","http://www.baidu.com"]},{"keywords":"userkw_sendmsg","datas":["get","http://www.baidu.com"]}
              ]
              }
  #调用测试用例执行函数，如果网页可以写成一个服务
  run(jsondata)