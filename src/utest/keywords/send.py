from  drivers.KippRequests import request
from SkiFramwork.log import logger

def remsg(mod,data):

    logger.info('in remsg')
    
    return request(data)