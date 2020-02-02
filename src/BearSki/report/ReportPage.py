from BearSki.utils.arguments import runArg
import time
import os
class reportBody(object):
    ALLTEXTDEMO=u'''
    <!doctype html>
    <html lang="en">
      <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Hello, Bootstrap Table!</title>

        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css" integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/" crossorigin="anonymous">
        <link rel="stylesheet" href="https://unpkg.com/bootstrap-table@1.15.5/dist/bootstrap-table.min.css">
        <script src="https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
        <script src="https://unpkg.com/bootstrap-table@1.15.5/dist/bootstrap-table.min.js"></script>
      </head>
      <body>
      <div class="container">
        <div class="jumbotron jumbotron-fluid">
          <div class="container">
          <h1 class="display-4">BearSki 自动化测试报告</h1>
          <p class="lead"></p>
          <p class="lead">执行结果汇总:
    '''
    MIDBODY=u'''
        </div>
        </div>
        <h3>用例执行情况：</h3>
        <HR  align=left width=500 color=#987cb9 SIZE=1/>
        <div width=400>
        <table id="table"
        data-toolbar="#toolbar"
      data-search="true"
      data-show-refresh="true"
      data-show-toggle="true"
      data-show-fullscreen="true"
      data-show-columns="true"
      data-show-columns-toggle-all="true"
      data-detail-view="true"
      data-show-export="true"
      data-click-to-select="true"
      data-detail-formatter="detailFormatter"
      data-minimum-count-columns="2"
      data-show-pagination-switch="true"
      data-pagination="true"
      data-id-field="id"
      data-page-list="[10, 25, 50, 100, all]"
      data-show-footer="true"
        >
      <thead>
        <tr>
          <th data-field="id">ID</th>
          <th data-field="suitname">SUITNAME</th>
          <th data-field="casename">CASENAME</th>
          <th data-field="result">RESULT</th>
        </tr>
      </thead>
    </table>
    </div>
    </div>
    <script>

      var $table = $('#table')
      $(function() {
        var data = 
      '''
    ENDPART=u'''
        $table.bootstrapTable({data: data})
      })

    </script>
    <script>
      function detailFormatter(index, row) {
        var html = []
        $.each(row, function (key, value) {
          if(key=='message'){
            
            for(line in value){
                html.push('<p><b>' + value[line] + '</p>')
            }
              
            
            
          }
        
        })
        return html.join('')
      }
    </script>

      </body>
    </html>
    '''
    result_data=[]

    SUMMARYTEXT=u'''
    <span class="badge badge-success">Pass</span> &ensp;'''
    S1=u'''&ensp;
          <span class="badge badge-danger">Error</span> &ensp; '''
    S2=u''' &ensp;<span class="badge badge-warning">Failure</span>  &ensp;'''
    S3=u''' </p>
    '''
    summary_all=''
    report=''
    def __init__(self):
      self.rags=runArg()
    def add_summary(self,summary_data):
      # self.summary_data={'success':sd,'error':ed,'warning':wd}
      self.summary_all=self.SUMMARYTEXT+summary_data['success']+self.S2+summary_data['warning']+self.S1+summary_data['error']+self.S3
    
    def generate_report(self):
      self.report=self.ALLTEXTDEMO+self.summary_all+self.MIDBODY+str(self.result_data)+self.ENDPART
    
    def add_one_test_result(self,result_data):
      self.result_data.append(result_data)

    def writ_report(self):
      today_now=time.strftime("%Y%m%d_%H%M%S", time.localtime())
      (filepath, tempfilename) = os.path.split(self.rags.report_path)
      (filename, extension) = os.path.splitext(tempfilename)
      if not os.path.exists(filepath):
        os.makedirs(filepath)
      outfilename=self.rags.report_path
      if self.rags.report_add_time:
        outfilename=os.path.join(filepath,filename+"_"+today_now+extension)
      fo = open(outfilename, "w+",encoding='utf8')
      fo.write(self.report)
      fo.close
 
# if __name__ == '__main__':
  
#   rb=reportBody()
#   summary_test_data={'success':'1','error':'2','warning':'3'}
#   rb.add_summary(summary_test_data)
#   rdata={
#             'id': 0,
#             'casename': 'test 0',
#             'result': 'pass',
#             'message':['2019-09-27 14:36:48,954 INFO 开始执行测试',
#                       '2019-09-27 15:07:42,807 INFO in ask baidu!',
#                       '2019-09-27 15:08:02,280 INFO <Response [200]>',
#                       '2019-09-27 15:08:02,808 INFO Creating Session using : alias=baidu, url=http://www.baidu.com, headers={},                     cookies=None, auth=None, timeout=None, proxies=None, verify=False,                     debug=0 ',
#                       '2019-09-27 15:08:02,808 INFO Creating Session using : alias=baidu, url=http://www.baidu.com, headers={},                     cookies=None, auth=None, timeout=None, proxies=None, verify=False,                     debug=0 '
#             ]
#           }
#   rb.add_one_test_result(rdata)
#   rb.add_one_test_result(rdata)
#   rb.add_one_test_result(rdata)
#   rb.generate_report()
#   rb.writ_report()
