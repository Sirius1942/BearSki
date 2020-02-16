# -*- encoding: utf-8 -*-
'''
@File    :   singleton.py
@Time    :   2019/11/28 11:50:09
@Author  :   Sirius 
'''

class Singleton(object): 
    def __init__(self, cls): 
        self._cls = cls 
    def __call__(self, *args, **kwargs): 
        try: 
            return self._instance 
        except AttributeError: 
            self._instance = self._cls() 
            return self._instance 