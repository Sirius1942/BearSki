import unittest
import BearSki.RunUnittest as rut
from BearSki.log import logger
from BearSki.report.LocalReportRunner import LocalReportRunner
import time
import sys
import logging
from BearSki.utils.arguments import runArg 

def get_test_cases(dirpath,name="test_",isrunonecase=False):
    test_cases = unittest.TestSuite()
    # 测试用例使用"ski_"开头命名
    if isrunonecase:
        # 执行单条用例，顺序为 目录名 文件名 类名 方法名 中间"." 间隔 例如："testcase.debug_test_user.TestUserLogin.test_login"
       suite=unittest.TestLoader().loadTestsFromName(dirpath)
       test_cases.addTests(suite)
       return test_cases

    else:
        suites = unittest.defaultTestLoader.discover(dirpath, name+'*.py', top_level_dir=dirpath)
        for suite in suites:
          test_cases.addTests(suite)
        return test_cases

if __name__ == '__main__':
    rag=runArg()
    report_type='h'
    isrunonecase='True'
    casepath='utest.testcase.test_send.TestSendMessage.test_send_use_robotframework_requestlibary'
    casename='test_send'
    cases = get_test_cases(casepath,casename,isrunonecase)
    now = time.strftime("%Y-%m-%d %H_%M_%S")  # 报告生成时间
    test_reports_address = './utest/report'      # 测试报告存放位置
    filename = './utest/report/' + now + 'report.html'  # 设置报告文件名

    if(report_type=='text'):
        logger.info("开始执行测试,报告输出模式text")
        runner=unittest.TextTestRunner()
        runner.run(cases)
    elif(report_type=='html'):
        logger.info("开始执行测试,报告输出模式html")
        lruner=LocalReportRunner()
        lruner.run(cases)
    


        
    


