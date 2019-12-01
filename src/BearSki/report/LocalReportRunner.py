import datetime
import io
import sys
import time
import unittest
from xml.sax import saxutils
from BearSki.report.ReportPage import  reportBody



TestResult = unittest.TestResult

class OutputRedirector(object):
    """ Wrapper to redirect stdout or stderr """
    def __init__(self, fp):
        self.fp = fp

    def write(self, s):
        self.fp.write(s)

    def writelines(self, lines):
        self.fp.writelines(lines)

    def flush(self):
        self.fp.flush()

stdout_redirector = OutputRedirector(sys.stdout)
stderr_redirector = OutputRedirector(sys.stderr)

class _TestResult(TestResult):
    
    def __init__(self, verbosity=1):
        TestResult.__init__(self)
        self.stdout0 = None
        self.stderr0 = None
        self.success_count = 0
        self.failure_count = 0
        self.error_count = 0
        self.verbosity = verbosity
        self.result = []

    def startTest(self, test):
        TestResult.startTest(self, test)
        # just one buffer for both stdout and stderr
        self.outputBuffer = io.StringIO()
        stdout_redirector.fp = self.outputBuffer
        stderr_redirector.fp = self.outputBuffer
        self.stdout0 = sys.stdout
        self.stderr0 = sys.stderr
        sys.stdout = stdout_redirector
        sys.stderr = stderr_redirector

    def complete_output(self):
        """
        Disconnect output redirection and return buffer.
        Safe to call multiple times.
        """
        if self.stdout0:
            sys.stdout = self.stdout0
            sys.stderr = self.stderr0
            self.stdout0 = None
            self.stderr0 = None
        return self.outputBuffer.getvalue()

    def stopTest(self, test):
        self.complete_output()

    def addSuccess(self, test):
        self.success_count += 1
        TestResult.addSuccess(self, test)
        output = self.complete_output()
        self.result.append(('pass', test, output, ''))
        
        
        
    def addError(self, test, err):
        self.error_count += 1
        TestResult.addError(self, test, err)
        _, _exc_str = self.errors[-1]
        output = self.complete_output()
        self.result.append(('error', test, output, _exc_str))
        

    def addFailure(self, test, err):
        self.failure_count += 1
        TestResult.addFailure(self, test, err)
        _, _exc_str = self.failures[-1]
        output = self.complete_output()
        self.result.append(('Failure', test, output, _exc_str))

class LocalReportRunner():
    """
    """
    DEFAULT_TITLE='BearSki 自动化测试报告'
    DEFAULT_DESCRIPTION=''
    def __init__(self, stream=sys.stdout, verbosity=1, title=None, description=None):
        self.stream = stream
        self.verbosity = verbosity
        if title is None:
            self.title = self.DEFAULT_TITLE
        else:
            self.title = title
        if description is None:
            self.description = self.DEFAULT_DESCRIPTION
        else:
            self.description = description
        self.startTime = datetime.datetime.now()


    def run(self, test):
        "Run the given test case or test suite."
        result = _TestResult(self.verbosity)
        test(result)
        self.stopTime = datetime.datetime.now()
        # print(result)
        self.generateReport(test, result)
        #print(sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime))
        return result

    def sortResult(self, result_list):
        # unittest does not seems to run in any particular order.
        # Here at least we want to group them together by class.
        rmap = {}
        classes = []
        for n,t,o,e in result_list:
            cls = t.__class__
            if not cls in rmap:
                rmap[cls] = []
                classes.append(cls)
            rmap[cls].append((n,t,o,e))
        r = [(cls, rmap[cls]) for cls in classes]
        return r


    def getlogMessage(self, message):

        return message.split('\n')

    def generateReport(self, test, result):
        rb=reportBody()
        summary_test_data={'success':str(result.success_count),'error':str(result.error_count),'warning':str(result.failure_count)}
        rb.add_summary(summary_test_data)
        # print(result.result)
        
        for tid, (n,t,o,e) in enumerate(result.result):
            # print(o)
            fullname=t.id()
            casename=t.id().split('.')[-1]
            suitlong=len(fullname)-len(casename)-1
            rdata={'id': tid+1,
                'suitname':fullname[0:suitlong],
                'casename':casename,
                'result':n,
                'message':self.getlogMessage(o)}
            rb.add_one_test_result(rdata)
        rb.generate_report()
        rb.writ_report()
       
        