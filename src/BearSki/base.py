# -*- coding:utf-8 -*-
import json
import os
import importlib.util
import importlib
import inspect
from importlib import import_module
from BearSki.CommonData import SkiGlobalData
from BearSki.log import logger

class Ski():
    class case():
        def __init__(self):
            # print('__case init__')
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
            scd=SkiGlobalData()
            conf=scd.get_setting_data()
            full_modules=conf[keyword]
            self.result=self.__run(full_modules,*arg,**kws)
            logger.info(self.result)
        def __run(self,kw_path,*arg,**kws):
            try:
                modules=self.__getModules(kw_path)
            
            except Exception:
                logger.error("error,does not find  modules")
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
                print("error",error)
                
                return False
            if module_spec is None:
                # print("Module :{} not found".format(module_name))
                # print("false")
                return False

            else:
                # print("Module:{} can be imported!".format(module_name))
                # print("true")
                return True
            

        