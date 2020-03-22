from BearSki.utils.singleton import Singleton

@Singleton
class runArg(object):
  
  def __init__(self,mode='allrun',
                    case_path='./testcase',
                    report_path='./runner/result.html',
                    config_path='./config.json',
                    jsonfile_path='./SkiSetting.json',
                    report_mode='text',
                    testsuit_runner='unittest'):
    self.report_mode=report_mode
    self.mode=mode
    self.case_path=case_path
    self.case_name=''
    self.report_path=report_path
    self.config_path=config_path
    self.jsonfile_path=jsonfile_path
    self.testsuit_runner=""

  def setValueFromJson(self,jsonstr):
    self.mode=jsonstr['m']
    self.report_mode=jsonstr['r']
    self.report_path=jsonstr['o']
    self.case_name = jsonstr['n']
    self.case_path = jsonstr['p']
    self.jsonfile_path=jsonstr['j']
    self.testsuit_runner=jsonstr['testsuit.runner']
    if 'runner.addtime.now' in jsonstr:
      self.report_add_time=jsonstr['report.addtime.now']
    else:
      self.report_add_time=False
    if 'auto.case.path' in jsonstr:
      self.auto_case_path=jsonstr['auto.case.path']
    else:
      self.auto_case_path=False
    if 'auto.model.path' in jsonstr:
      self.auto_model_path=jsonstr['auto.model.path']
    else:
      self.auto_model_path=False
    
  def getJsonString(self):
    message={
      "report_mode":self.report_mode,
      "mode":self.mode,
      "case_path":self.case_path,
      "case_name":self.case_name,
      "report_path":self.report_path,
      "config_path":self.config_path,
      "json_path":self.jsonfile_path,
      "runner.addtime.now":self.report_add_time,
      "auto.case.path":self.auto_case_path,
      "auto.model.path":self.auto_model_path,
      "testsuit.runner":self.testsuit_runner
    }
    return message
