import requests

	# 发送消息格式：｛"url"："www.baidu.com"｝
def request(data):
    r = requests.get(url="http://www.baidu.com")    # 最基本的GET请求
    return r
    # print(r.status_code)    # 获取返回状态
    # r = requests.get(url='http://dict.baidu.com/s', params={'wd':'python'})   #带参数的GET请求
    # print(r.url)
    # print(r.text)  
