# -*- encoding: utf-8 -*-
'''
@File    :   g4.py
@Time    :   2020/01/27 01:12:31
@Author  :   chenjiusi 
'''
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import hashlib
import time
import json

LOG_LINE_NUM = 0

class MY_GUI():
    def __init__(self,init_window_name):

        self.init_window_name = init_window_name
        self.row_1=1
        self.row_2=2
        self.row_3=3
        self.row_4=7
        self.row_5=8
        
        self.row_rowspan_1=2
        self.row_rowspan_2=2
        
        self.column_1=0
        self.column_2=4
        self.column_row1_2=1
        self.column_row1_3=7
        self.column_row1_4=8
        self.column_row1_5=9

        self.row3_columnspan_1=4
        self.row3_columnspan_2=6
        self.column_2_columnspan=5

        self.pdx=5
        self.pady=5

        self.text_height=20

        # 读取的harfile文件内容 {modelname + dic}
        self.harfile={}

    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("BearSki 用例生成工具 V 0.0.1")   #窗口名
        self.init_window_name.geometry('960x680')  #窗口大小设置
        self.init_window_name["bg"] = "#F5F5F5"
        self.init_window_name.grid_columnconfigure(0,weight=1)
        self.init_window_name.grid_rowconfigure(0,weight=1)

        #row 1
        self.init_data_label = Label(self.init_window_name, text="Har文件地址：")
        self.init_data_label.grid(row=self.row_1, column=self.column_1,sticky=N+W,padx=self.pdx,pady=self.pady)
        self.har_path_input=Entry(self.init_window_name,width=25)
        self.har_path_input.grid(row=self.row_1,column=self.column_row1_2,sticky=N+E,padx=self.pdx,pady=self.pady)
        self.get_har_text = ttk.Button(self.init_window_name, text="读取文件",command=self.openfiles)
        self.get_har_text.grid(row=self.row_1, column=self.column_2,sticky=N+W,padx=self.pdx,pady=self.pady)
        self.put_one_request = ttk.Button(self.init_window_name, text="生成用例",command=self.createOneCase)  # 调用内部方法  加()为直接调用
        self.put_one_request.grid(row=self.row_1, column=self.column_row1_4,sticky=N+W,padx=self.pdx,pady=self.pady)
        self.put_all_request = ttk.Button(self.init_window_name, text="批量生成用例",command=self.createAllCase)  # 调用内部方法加()为直接调用
        self.put_all_request.grid(row=self.row_1, column=self.column_row1_5,sticky=N+W,padx=self.pdx,pady=self.pady)

        #row 2
        self.result_data_label = Label(self.init_window_name, text="请求目录:")
        self.result_data_label.grid(row=self.row_2, column=self.column_1, columnspan=self.row3_columnspan_1,sticky=N+W,padx=self.pdx,pady=self.pady)
        self.result_data_label1 = Label(self.init_window_name, text="发送的消息请求信息：")
        self.result_data_label1.grid(row=self.row_2, column=self.column_2,columnspan=self.row3_columnspan_2,sticky=N+W,padx=self.pdx,pady=self.pady)
        
        #row 3
        # # tree
        self.init_tree = ttk.Treeview(self.init_window_name, show="headings", columns=('col1'))
        self.init_tree.heading('col1', text='modelname')
        self.init_tree.column('col1', width=350, anchor='nw')
        self.init_tree.grid(row=self.row_3, column=self.column_1, rowspan=self.row_rowspan_1, columnspan=self.row3_columnspan_1,sticky=N+W,padx=self.pdx)

        self.result_data_Text = Text(self.init_window_name,height=self.text_height)  #处理结果展示
        self.result_data_Text.grid(row=self.row_3, column=self.column_2, rowspan=self.row_rowspan_1, columnspan=self.row3_columnspan_2,sticky=N+W,padx=self.pdx)

        #row 4
        self.log_label = Label(self.init_window_name, text="日志:")
        self.log_label.grid(row=self.row_4, column=self.column_1,sticky=N+W,padx=self.pdx)
        self.result_data_label1 = Label(self.init_window_name, text="获取的返回值:")
        self.result_data_label1.grid(row=self.row_4, column=self.column_2,sticky=N+W,padx=self.pdx)

        #row 5
        self.log_data_Text = Text(self.init_window_name,height=self.text_height)  # 日志框
        self.log_data_Text.grid(row=self.row_5, column=self.column_1, columnspan=self.row3_columnspan_1,rowspan=self.row_rowspan_2,sticky=N+W,padx=self.pdx)
        self.result_data_Text1 = Text(self.init_window_name,height=self.text_height)#处理结果展示
        self.result_data_Text1.grid(row=self.row_5, column=self.column_2, rowspan=self.row_rowspan_2, columnspan=self.row3_columnspan_2,sticky=N+W,padx=self.pdx)

        #事件件绑定
        self.init_tree.bind("<Double-1>", self.onDBClick)

    def onDBClick(self,event):
        item = self.init_tree.selection()[0]
        modelname=self.init_tree.item(item, "values")
        print ("you clicked on name is :{0} ".format(modelname[0]))
        # print(self.harfile)
        req_str=self.harfile[modelname[0]]
        self.getOneMessage(req_str)
    

    def openfiles(self):
      harfilename = filedialog.askopenfilename(title='打开Har文件', filetypes=[('har', '*.har'), ('All Files', '*')],initialdir='./')

      self.har_path_input.insert(0,harfilename)

      fo = open(harfilename, "r+",encoding='utf8')
      jstr=json.loads(fo.read())
      req_list=jstr['log']['entries']
      i=0
      self.harfile={}
      for req_index in req_list:
        #   print(['request'])
          urldata=req_index['request']['url'].split('/')[3:]
          newrul='/'.join(str(i) for i in urldata)
          self.init_tree.insert('',i,values=(newrul))
        #   print(newrul)
          self.harfile[newrul]=req_index
          i=i+1
    #   print(self.harfile)

    def getOneMessage(self,req):
        # req,res="",""
        req,res=self.getMessage(req)
        self.result_data_Text.delete(1.0,END)
        self.result_data_Text.insert(1.0,json.dumps(req, sort_keys=True, indent=4, separators=(',', ': '),ensure_ascii=False))
        self.result_data_Text1.delete(1.0,END)
        self.result_data_Text1.insert(1.0,json.dumps(res, sort_keys=True, indent=4, separators=(',', ': '),ensure_ascii=False))
    
    def createAllCase(self):
        for onereq in self.harfile:
            req,res=self.getMessage(self.harfile[onereq])
            self.createTestCase(req,res)
    #功能函数
    def getMessage(self,req):
        # src = self.init_data_Text.get(1.0,END).strip().replace("\n","").encode()
        #print("src =",src)
        if req:
            try:
                request_str=req['request']
                respone_str=req['response']
                # self.result_data_Text.delete(1.0,END)
                # self.result_data_Text.insert(1.0,json.dumps(request_str, sort_keys=True, indent=4, separators=(',', ': '),ensure_ascii=False))
                # self.result_data_Text1.delete(1.0,END)
                # self.result_data_Text1.insert(1.0,json.dumps(respone_str, sort_keys=True, indent=4, separators=(',', ': '),ensure_ascii=False))
                # req=json.dumps(request_str, sort_keys=True, indent=4, separators=(',', ': '),ensure_ascii=False)
                # res=json.dumps(respone_str, sort_keys=True, indent=4, separators=(',', ': '),ensure_ascii=False)
                return request_str,respone_str
                self.write_log_to_Text("数据解析成功")
            except Exception as e:
                print(e)
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"数据解析失败")

        else:
            self.write_log_to_Text("ERROR:str_trans_to_md5 failed")

    def initData(self):
        fo = open("h13.har", "r+",encoding='utf8')
        jstr=json.loads(fo.read())
        self.init_data_Text.insert(1.0,jstr)
    
    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time
    
    def createOneCase(self):
        req_str=json.loads(self.result_data_Text.get(1.0,END))
        res_str=json.loads(self.result_data_Text1.get(1.0,END))
        self.createTestCase(req_str,res_str)
    

    def createTestCase(self,req_str,res_str):
        # print(req_str)
        urldata=req_str['url'].split('/')[3:]
        newrul='/'.join(str(i) for i in urldata)
        req_str['url']=newrul
        # print(req_str)
        self.write_log_to_Text("获取API接口：{0}".format(newrul))
        modelpath="../testdata/model/"
        casepath="../testcase/"
        modelname=newrul.replace('/','_')[:-1]
        self.writeFile(modelpath+modelname+'_model.json',json.dumps(req_str, sort_keys=True, indent=4, separators=(',', ': '),ensure_ascii=False))
        self.writeFile(modelpath+modelname+'_rep.json',json.dumps(res_str, sort_keys=True, indent=4, separators=(',', ': '),ensure_ascii=False))
        testcase='''
    
# coding=utf-8
import time
import unittest
from BearSki.base import Ski
from BearSki.base import DT
import logging
import json

class test_${modelname}(unittest.TestCase,Ski):

    def setUp(self):
        self.logger=logging.getLogger("test_${modelname}")
    def tearDown(self):
        pass
    @Ski.case()
    def case_${modelname}(self):
        model_name="${modelname}"
        self.logger.info("in case_${modelname}")
        res=self.step("requestFromModel",model_name+'_model.json')
        fo = open("${model_file_path}"+model_name+"_rep.json", "r+",encoding='utf8')
        jstr=json.loads(fo.read())
        self.assertEqual(jstr['status'],res.result.status_code)
        self.logger.info("login res {0}".format(res))
'''
        newcase=testcase.replace("${modelname}",modelname).replace("${model_file_path}",modelpath)
        
        self.writeFile(casepath+"test_"+modelname+'.py',newcase)

    def writeFile(self,filename,context):
        fo= open(filename,"w+")
        # print(context)
        fo.write(context)
        fo.close



    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)


def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()
    # ZMJ_PORTAL.initData()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示
    


gui_start()


