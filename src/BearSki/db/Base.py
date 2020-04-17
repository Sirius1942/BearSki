import logging
from BearSki.utils.errors import *
from BearSki.CommonData import SkiGlobalData
from BearSki.utils.DataTable import getRowData,generate_data,generate_json_data,td_getJsonData

logger=logging.getLogger("BearSki.db")
class TestDataBase():
    vendor = 'unknown'
    display_name = 'unknown'
    queries_limit = 9000

    def __init__(self, settings_dict):
        self.connection = None
        self.settings_dict = settings_dict

    @property
    def queries(self):
        if len(self.queries_log) == self.queries_log.maxlen:
            logger.warning(
                "Limit for query logging exceeded, only the last {} queries "
                "will be returned.".format(self.queries_log.maxlen))
        return list(self.queries_log)

    def get_one_data(self,dataid,type):
        raise DataBaseError('subclasses of TestDataBase may require a get_connection_params() method')
    def get_datalist(self,dataid,type):
        raise DataBaseError('subclasses of TestDataBase may require a get_connection_params() method')
    def connect(self):
        pass


class ExcelFile(TestDataBase):
    def _init_(self,settings_dict):
        self.connection = None
        self.settings_dict = settings_dict

    def get_data(self,dataid,type,parms):
        if type == 'json':
            title, rowdata = getRowData(dataid,parms['PATH'])
            res = generate_json_data(title, rowdata)
            logger.info(u"依据索引[{0}]获取测试数据为:{1}，数据源为:{2}".format(dataid,res,parms['PATH']))
            return res
        elif type =='list':
            title, rowdata = getRowData(dataid,parms['PATH'])
            res = generate_data(title, rowdata)
            logger.info(u"依据索引[{0}]获取测试数据为:{1}，数据源为:{2}".format(dataid,res,parms['PATH']))
            return res
    def connect(self):
        pass

class JsonFile(TestDataBase):
    def _init_(self,settings_dict):
        self.connection = None
        self.settings_dict = settings_dict
    def get_data(self,dataid,type,parms):
        revalue = td_getJsonData(dataid, parms['PATH'])
        logger.info(u"依据索引[{0}]获取测试数据为:{1}，数据源为:{2}".format(dataid, revalue, parms['PATH']))
        return revalue
    def connect(self):
        pass










