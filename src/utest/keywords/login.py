import json
import logging
from BearSki.CommonData import SkiGlobalData
import requests

logger=logging.getLogger("kw.login")
BASE_URL=SkiGlobalData().get_global_data('BASE_URL')

# 提供通过用户名获取jwt的接口信息方法，获取后的认证字符串放在 SkiGlobalData 全局变量中
def login(body_data):
    url = '/auth/login/'
    headers = {'Content-Type': 'application/json'}
    # logger.info('in login！')
    login_user=body_data
    r = requests.post(url=BASE_URL+url,headers=headers,json=login_user)    # 最基本的GET请求
    logger.info("response is : {0}".format(r))
    logger.info("response is : {0}".format(r.text))
    result=json.loads(r.text)
    # global jwt_access
    # jwt_access[login_user['username']]=result['data']['access']
    SkiGlobalData().add_global_data({"Authorization":"Bearer "+result['detail']['token']})
    return r

def web_login(user_data):
  pass




  