import unittest
from bear.RunUnittest import HTMLTestRunner
import bear.RunUnittest as rut
from bear.log import logger
import time
import sys
import logging

def get_test_cases(dirpath):
    test_cases = unittest.TestSuite()
    # 测试用例使用"ski_"开头命名
    suites = unittest.defaultTestLoader.discover(dirpath, 'ski_*.py', top_level_dir=dirpath)
    for suite in suites:
        test_cases.addTests(suite)
    return test_cases

if __name__ == '__main__':

    logger.info("开始执行测试")
    cases = get_test_cases('./testcase')
    now = time.strftime("%Y-%m-%d %H_%M_%S")  # 报告生成时间
    test_reports_address = '../report'      # 测试报告存放位置
    filename = './report/' + now + 'report.html'  # 设置报告文件名
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u'自动化测试', description=u'详细测试结果如下:')
    runner.run(cases)
    fp.close()


