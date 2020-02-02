import json
import logging
from BearSki.CommonData import SkiGlobalData
from utest.driver import d_requests
from BearSki.keywords.RequestModelKW import RequestModelCommondKW

logger=logging.getLogger("kw.requestModel")
BASE_URL=SkiGlobalData().get_global_data('BASE_URL')

# 提供通过用户名获取jwt的接口信息方法，获取后的认证字符串放在 SkiGlobalData 全局变量中
def runModel(jstr):
    rmckw=RequestModelCommondKW()
    r=rmckw.run(jstr)
    return r





