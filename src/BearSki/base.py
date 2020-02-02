# -*- coding:utf-8 -*-
import json
import os
import importlib.util
import importlib
import inspect
from importlib import import_module
from BearSki.CommonData import SkiGlobalData
from BearSki.utils.logger import SkiLogger
from BearSki.utils.DataTable import getRowData,generate_data,generate_json_data

class Ski():
    class case():
        def __init__(self):
            # print('__case init__')
            self.logger=SkiLogger("BearSki.base")
            self.logger.warn("bear.base 中的方法将被废弃，相关功能通过 bear.core 替代，建议将 from BearSki.base 修改为 from BearSki.core")
            scd=SkiGlobalData()
        def __call__(self,func):
                def __deco(self,*arg,**kws):
                    # print("before %s called [%s],[%s]." % (func.__name__, arg,kws))
                    result=func(self,*arg,**kws)
                    # print("  after %s called [%s],[%s]." % (func.__name__, arg,kws))
                    return result
                return __deco

    class step():
        def __init__(self,keyword,*arg,**kws):
            self.logger=SkiLogger("BearSki.step")
            scd=SkiGlobalData()
            conf=scd.get_setting_data()
            full_modules=conf[keyword]
            self.result=self.__run(full_modules,*arg,**kws)
            # self.logger.debug(self.result)
        def __run(self,kw_path,*arg,**kws):
            try:
                modules=self.__getModules(kw_path)
            
            except Exception:
                self.logger.error("error,does not find  modules")
                return None
            
            fun_list=kw_path[len(modules)+1:].split('.')
            
            return self.__getObject(modules,fun_list)(*arg,**kws)

        def __getObject(self,modules,fun_list):
            
            obj= import_module(modules)
            child_obj=getattr(obj,fun_list[0])
            temp_cls_name=fun_list[0]
            for key in fun_list[1:]:
                if inspect.isclass(child_obj):
                    # print("this is a class")
                    temp_cls=SkiGlobalData().get_step_class_instance(temp_cls_name)
                    if temp_cls is None:
                        child_obj=child_obj()
                        SkiGlobalData().set_step_class_instance(temp_cls_name,child_obj)
                    else:
                        child_obj=temp_cls
                child_obj=getattr(child_obj,key)
                temp_cls_name=key
            return child_obj

        def __getModules(self,kw_path):
            # print(kw_path)
            if kw_path.find('.')==-1:
                if self.__ismodule(kw_path):
                    return modules
                else:
                    raise Exception("all error,does not find  modules")
            kw=kw_path.split('.')[-1]
            modules=kw_path[0:kw_path.rindex(kw)-1]  #rindex 为了应对报名重名 从后向前计算
            flag=self.__ismodule(modules)
            # print(flag)
            if flag:
                # print(modules)
                return modules
            else:
                # print(modules)
                return self.__getModules(modules)

        def __ismodule(self,module_name):

            # print("++++++ is module ++++")
            # print(module_name)
            # print("====== is module =====")
            module_spec=None
            try:
                module_spec = importlib.util.find_spec(module_name)
            except Exception as error:
                # print(error)
                logger.error("error",error)
                
                return False
            if module_spec is None:
                # print("Module :{} not found".format(module_name))
                # print("false")
                return False

            else:
                # print("Module:{} can be imported!".format(module_name))
                # print("true")
                return True

class DT(object):
    def __init__(self,str_data,type="excel"):
        # print('__case init__')
        self.str_data=str_data
        self.logger=SkiLogger("BearSki.DataTable")
        self.logger.warn("bear.base 中的方法将被废弃通过 bear.core 替代，建议将 from BearSki.base 修改为 from BearSki.core")
        self.basedata=SkiGlobalData().get_datatable_config()
        self.type=type

    def list(self):
        if self.type=='excel':
            return self._excel_list()
    def json(self):
        if self.type=='excel':
            return self._excel_list()
        else:
            return self._json_json()
    
    def _excel_list(self):
        title,rowdata=getRowData(self.str_data, self.basedata["db_path"])
        res=generate_data(title,rowdata)
        self.logger.debug(u"依据索引[{0}]获取测试数据为:{1}，数据源为:{2}".format(self.str_data,res, self.basedata["db_path"]))
        return res
    def _excel_json(self):
        title,rowdata=getRowData(self.str_data, self.basedata["db_path"])
        res=generate_json_data(title,rowdata)
        self.logger.debug(u"依据索引[{0}]获取测试数据为:{1}，数据源为:{2}".format(self.str_data,res, self.basedata["db_path"]))
        return res




            

        