from driver import d_requests
from BearSki.utils.logger import SkiLogger

logger=SkiLogger('keywords.send')

def askbaidu(mod,data):
    logger.info('in ask baidu！')
    r = d_requests.get(url=data)    # 最基本的GET请求
    return r