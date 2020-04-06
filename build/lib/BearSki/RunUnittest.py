import unittest
import time
from BearSki.runner.LocalReportRunner import LocalReportRunner
from BearSki.core import Ski

class RunUnittest(object):

    def __init__(self):
       pass
        
    def get_test_cases(self,dirpath,name="test_",isrunonecase=False):
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
    @Ski.init()
    def runTest(self,runArg):
        isrunonecase=False
        if runArg.mode=='onecase':
            isrunonecase=True
        casepath=runArg.case_path
        casename=runArg.case_name
        cases = self.get_test_cases(casepath,casename,isrunonecase)
        now = time.strftime("%Y-%m-%d %H_%M_%S")  # 报告生成时间
        if(runArg.report_mode=='text'):
            # self.logger.info("开始执行测试,报告输出模式text")
            runner=unittest.TextTestRunner()
            runner.run(cases)
        elif(runArg.report_mode=='html'):
            # self.logger.info("开始执行测试,报告输出模式html")
            lruner=LocalReportRunner()
            lruner.run(cases)
            # self.logger.info("测试完成,报告输出模式html")

