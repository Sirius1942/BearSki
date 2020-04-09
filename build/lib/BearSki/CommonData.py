import json
import os
from BearSki.utils.arguments import runArg 
from BearSki.utils.singleton import Singleton
from BearSki.utils.errors import *


@Singleton
class SkiGlobalData(object):
    def __init__(self):
        self.classes={}
        self.rags=runArg()
        self.config=self._getConfigObject(self.rags)
        #  记录当前用例执行的模块名和用例名
        self.runCaseObject = []
    def get_step_class_instance(self,cls_name):

        if cls_name in self.classes:
            return self.classes[cls_name]
        else:
            return None
    def set_step_class_instance(self,cls_name,cls):
        self.classes[cls_name]=cls

    def get_setting_data(self):
        return self.config.get_setting_data()

    def get_global_all_data(self):
        return self.config.get_global_all_data()

    def get_global_data(self,value):
        return self.config.get_global_data(value)

    def add_global_data(self,data):
        self.config.add_global_data(data)

    def get_datatable_config(self):
        return self.config.get_datatable_config()
    def get_initdata(self,name):
        return self.config.get_initdata(name)
    def get_test_database(self):
        return self.config.get_test_database()
    def get_test_database_case_mapping(self):
        return self.config.get_test_database_case_mapping()
    ## 记录当前用例运行模块和用例。 session，moudel，function 3个级别。

    def setup_runObject(self,name):
        self.runCaseObject.append(name)

    def teardown_runObject(self):
        # 最后一个是default，保留在对象中避免被释放
        if len(self.runCaseObject)>1:
            self.runCaseObject.pop()
        else:
            pass

    def get_database_parms(self):
        if len(self.runCaseObject)==1:
            # 直接返回默认数据库配置
            return self.get_test_database()[self.runCaseObject[0]]
        data_mapping=self.get_test_database_case_mapping()
        reCaseObject=self.runCaseObject.reverse()
        for name in reCaseObject:
            if name in data_mapping:
                return self.get_test_database()[self.runCaseObject[name]]
        raise DataBaseError("获取数据对应配置参数出错，请检查Setting文件中是否配置正确。")

    def _check_isin_datamapping(self,name):
        pass

    def _getConfigObject(self,rags):
        # jsonfile_path 为老版本遗留名称 老版本只支持 skisetting.json 一种格式。1.5.0版本之后扩展支持多种版本的配置文件。变量名未变
        (configfile_path, configfile_name) = os.path.split(rags.jsonfile_path)
        extname = configfile_name.split(".")[-1:]  # 获取扩展名用于判断
        if extname[0] == "json":
            return JsonConfigObject(rags)
        elif extname[0] =="py":
            return PyfileConfigObject(rags)


class ConfigObject():

    def __init__(self,rags):
        self.config={}

    def get_setting_data(self):
        try:
            return self.config.KW_ROUTER
        except:
            raise SettingFileError("没有找到{0}配置，请检查配置文件，是否包含{0} 配置".format('KW_ROUTER'))

    def get_global_all_data(self):
        try:
            return self.config.GLOBAL_VARIABLE
        except:
            raise SettingFileError("没有找到{0}配置，请检查配置文件，是否包含{0} 配置".format('GLOBAL_VARIABLE'))

    def get_global_data(self, value):
        try:
            return self.config.GLOBAL_VARIABLE[value]
        except:
            raise SettingFileError("没有找到{0}.{1}配置，请检查配置文件，是否包含{0}.{1} 配置".format('GLOBAL_VARIABLE',value))

    def add_global_data(self, data):
        try:
            for s in data:
                self.config.GLOBAL_VARIABLE[s] = data[s]
        except:
            raise SettingFileError("添加全局变量异常")

    def get_datatable_config(self):
        try:
            return self.config.DATATABLE
        except:
            raise SettingFileError("没有找到{0}配置，请检查配置文件，是否包含{0} 变量".format('DATATABLE'))

    def get_initdata(self, name):
        try:
            return self.config.initdata['name']
        except:
            raise SettingFileError("没有找到{0}配置，请检查配置文件，是否包含{0} 配置".format('TEST_DATABASES'))
    def get_test_database(self):
        try:
            return self.config.TEST_DATABASES
        except Exception as e:
            raise SettingFileError(e,"没有找到{0}配置，请检查配置文件，是否包含{0} 配置 config ：{1}".format('TEST_DATABASES',self.config))
    def get_test_database_case_mapping(self):
        try:
            return self.config.TEST_DATABASE_CASE_MAPPING
        except:
            raise SettingFileError("没有找到{0}配置，请检查配置文件，是否包含{0} 配置".format('TEST_DATABASE_APPS_MAPPING'))

class JsonConfigObject(ConfigObject):

    def __init__(self,rags):
        # jsonfile_path 为老版本遗留名称 老版本只支持 skisetting.json 一种格式。1.5.0版本之后扩展支持多种版本的配置文件。变量名未变
        # (configfile_path, configfile_name) = os.path.split(rags.jsonfile_path)
        # extname = configfile_name.split(".")[-1:]  # 获取扩展名用于判断
        # if extname == "json":
        f = open(rags.jsonfile_path)
        conf = json.load(f)
        self.config=conf

    def get_setting_data(self):
        return self.config['routers']
    def get_global_all_data(self):
        return self.config['global_variable']
    def get_global_data(self,value):
        try:
            returndata = self.config['global_variable'][value]
            return returndata
        except Exception:
            return  None
    def add_global_data(self,data):
        for s in data:
            self.config['global_variable'][s]=data[s]
    def get_datatable_config(self):
        returndata = self.config['datatable']
        return returndata
    def get_initdata(self,name):
        try:
            returndata=self.config['initdata'][name]
            return returndata
        except Exception as e:
            return None


class PyfileConfigObject(ConfigObject):
    def __init__(self,rags):
        (configfile_path, configfile_name) = os.path.split(rags.jsonfile_path)
        extname = configfile_name.split(".")
        try:
            self.config=__import__(extname[0], fromlist=True)
        except Exception as e:
            raise SettingFileError(e,"读取配置文件异常")

