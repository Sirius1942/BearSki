#encoding=utf-8
import os
import logging
import BearSki.report.LocalReportRunner as rut
from BearSki.CommonData import SkiGlobalData
from BearSki.utils.singleton import Singleton
from BearSki.utils.arguments import runArg

class LoggerBaseConfig(object):
   
    def __init__(self):
       
        self.level=get_level()
        self.filename=get_log_path()
        self._initlogger()

    def _initlogger(self):
        # pass
        rflogger=SkiLogger('RobotFramework')
    def _htmlRunner_logset(self):
        logging.basicConfig(stream=rut.stdout_redirector,
        format='[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s'
        )
        
@Singleton
class SkiLogger(object):
    def __init__(self, name=''):
        self.logger = logging.getLogger(name)
        self.loglevel=get_level()
        self.logger.setLevel(self.loglevel)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s')
        # 设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(self.loglevel)
        # 由于logging 的filehandler 与 stream 不能共存所以需要根据不同模式设置日志输出方式。
        if runArg().report_mode =='html':
            logging.basicConfig(stream=rut.stdout_redirector,
            format='[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s')
        if runArg().report_mode =='text':
            # 设置文件日志
            #logfile_path=SkiGlobalData().get_global_data("logfile_path")
            logfile_path=get_log_path()
            fh = logging.FileHandler(logfile_path)
            fh.setFormatter(fmt)
            fh.setLevel(self.loglevel)
            self.logger.addHandler(sh)
            self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
        
def get_level():
    reloglevel=get_logging_level(SkiGlobalData().get_global_data("log_level"))
    return reloglevel

def get_logging_level(levelmessage):

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

def get_log_path():
    config_json=SkiGlobalData().get_global_data("logfile_path")
    (logfile_path, logfile_name) = os.path.split(config_json)
    if logfile_path and logfile_name:
            isExists=os.path.exists(logfile_path)
            if not isExists:
                os.makedirs(logfile_path) 
    return config_json

# if __name__ == '__main__':
#     logger = Logger('test')
#     logger.debug('debug信息')
#     logger.info('info信息')
#     logger.war('warning信息')
#     logger.error('error信息')
#     logger.critical('critical信息')
