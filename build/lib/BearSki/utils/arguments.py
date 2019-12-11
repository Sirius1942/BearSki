from BearSki.utils.singleton import Singleton
@Singleton
class runArg(object):
  
  def __init__(self,mode='allrun',
                    case_path='./testcase',
                    report_path='./report/result.html',
                    config_path='./config.json',
                    jsonfile_path='./SkiSetting.json',
                    report_mode='text'):
    self.report_mode=report_mode
    self.mode=mode
    self.case_path=case_path
    self.case_name=''
    self.report_path=report_path
    self.config_path=config_path
    self.jsonfile_path=jsonfile_path

  def setValueFromJson(self,jsonstr):
    self.mode=jsonstr['m']
    self.report_mode=jsonstr['r']
    self.report_path=jsonstr['o']
    self.case_name = jsonstr['n']
    self.case_path = jsonstr['p']
    self.jsonfile_path=jsonstr['j']
    if 'report.addtime.now' in jsonstr:
      self.report_add_time=jsonstr['report.addtime.now']
    else:
      self.report_add_time=False
  def getJsonString(self):
    message={
      "report_mode":self.report_mode,
      "mode":self.mode,
      "case_path":self.case_path,
      "case_name":self.case_name,
      "report_path":self.report_path,
      "config_path":self.config_path,
      "json_path":self.jsonfile_path
    }
    return message
