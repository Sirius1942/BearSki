
from BearSki.case.TestResultSet import *
from BearSki.case.TestCaseSet import *
from BearSki.case.TestSuitSet import *
import logging
logger=logging.getLogger("BearSki.RunUnittest")



class SkiTestFactory():

    def run(self,args,commond):
        ts = eval(args.testsuit_runner)(args,commond)
        logger.info("Creating TestSuit..{0}".format(type(ts).__name__))
        logger.info("Commond List: {}".format(ts.getCommond()))
        logger.info("RunArguments List: {}".format(ts.getRunArg()))
        ts.runTest()
