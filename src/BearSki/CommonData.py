import json
import os
from BearSki.utils.arguments import runArg 
from BearSki.utils.singleton import Singleton
@Singleton
class SkiGlobalData(object):

    def __init__(self):
        self.classes={}
        self.rags=runArg()
        self.set_data=self.__get_conf_data()
        
        
    def get_step_class_instance(self,cls_name):

        if cls_name in self.classes:
            return self.classes[cls_name]
        else:
            return None
    def set_step_class_instance(self,cls_name,cls):
        self.classes[cls_name]=cls
    def get_setting_data(self):
        return self.set_data['routers']
    def __get_conf_data(self):
        f= open(self.rags.jsonfile_path)
        conf=json.load(f)
        return conf
    def get_global_all_data(self):
        return self.set_data['global_variable']
    def get_global_data(self,value):
        try:
            returndata = self.set_data['global_variable'][value]
            return returndata
        except Exception:
            return  None
    def add_global_data(self,data):
        for s in data:
            self.set_data['global_variable'][s]=data[s]
    def get_datatable_config(self):
        returndata = self.set_data['datatable']
        return returndata
    def get_initdata(self,name):
        try:
            returndata=self.set_data['initdata'][name]
            return returndata
        except Exception as e:
            return None
