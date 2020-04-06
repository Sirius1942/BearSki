#encoding=utf-8
import os
import logging

from BearSki.CommonData import SkiGlobalData
from BearSki.utils.singleton import Singleton

@Singleton
class SkiLoggerHandler(logging.Handler):
    runCaseid='System'
    caselogs={}
    def __init__(self):
        logging.Handler.__init__(self)
        self.caselogs[self.runCaseid]=""
    def emit(self, record):
        msg = self.format(record)
        self.addCaseMessage(self.runCaseid,msg)
    def addCaseMessage(self,caseid,msg):
        try:
            self.caselogs[caseid]=self.caselogs[caseid]+"\n"+msg
        except Exception:
            pass
    def delCaseMessage(self,caseid):
        try:
            self.runCaseid='System'
            self.caselogs.pop(caseid)
        except Exception:
            pass
    def getCaseMessage(self,caseid):
        return self.caselogs[caseid]

    def setRuncaseid(self,caseid):
        self.runCaseid=caseid
        self.caselogs[caseid] = ""

@Singleton
class SkiLogger(object):
    def __init__(self, name=''):
        self.logger = logging.getLogger(name)
        self.loglevel=self._get_level()
        self.logger.setLevel(self.loglevel)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s')
        # 设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(self.loglevel)
        # 由于logging 的filehandler 与 stream 不能共存所以需要根据不同模式设置日志输出方式。
        # 设置文件日志
        #logfile_path=SkiGlobalData().get_global_data("logfile_path")
        logfile_path=self._get_log_path()
        fh = logging.FileHandler(logfile_path)
        fh.setFormatter(fmt)
        fh.setLevel(self.loglevel)
        slh=SkiLoggerHandler()
        slh.setFormatter(fmt)
        slh.setLevel(self.loglevel)
        self.logger.addHandler(fh)
        self.logger.addHandler(sh)
        self.logger.addHandler(slh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
        
    def _get_level(self):
        reloglevel=self._get_logging_level(SkiGlobalData().get_global_data("log_level"))
        return reloglevel

    def _get_logging_level(self,levelmessage):

            if levelmessage.upper()=='DEBUG':
                return logging.DEBUG
            elif levelmessage.upper()=='ERROR':
                return logging.ERROR
            elif levelmessage.upper()=='WARNING':
                return logging.WARNING
            elif levelmessage.upper()=='CRITICAL':
                return logging.CRITICAL
            elif levelmessage.upper()=='FATAL':
                return logging.FATAL
            else:
                return logging.INFO

    def _get_log_path(self):
        config_json=SkiGlobalData().get_global_data("logfile_path")
        (logfile_path, logfile_name) = os.path.split(config_json)
        if logfile_path and logfile_name:
                isExists=os.path.exists(logfile_path)
                if not isExists:
                    os.makedirs(logfile_path)
        return config_json