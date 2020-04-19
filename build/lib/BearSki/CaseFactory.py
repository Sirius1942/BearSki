from BearSki.CommonData import SkiGlobalData
import logging
from BearSki.case.TestRunnerSet import *
logger=logging.getLogger("BearSki.RunUnittest")



class SkiTestFactory():

    def run(self,args,commond):
        #创建全局变量信息
        SkiGlobalData().setup_runObject('default')
        ts = eval(args.testsuit_runner)(args,commond)
        logger.info("Creating TestSuit..{0}".format(type(ts).__name__))
        logger.info("Commond List: {}".format(ts.getcommand()))
        logger.info("RunArguments List: {}".format(ts.getRunArg()))
        ts.runTest()
