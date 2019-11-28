import requests
from BearSki.log import logger

def askbaidu(mod,data):

    logger.info('in ask baidu！')
    r = requests.get(url=data)    # 最基本的GET请求
    return r