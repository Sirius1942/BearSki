from tkinter import *
from tkinter import ttk
import hashlib
import time
import json

LOG_LINE_NUM = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name
        

    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("BearSki 用例生成工具 V 0.0.1")           #窗口名
        self.init_window_name.geometry('960x681+10+10')  #窗口大小设置
        self.init_window_name["bg"] = "#F5F5F5"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        self.init_data_label = Label(self.init_window_name, text="Har数据")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self.init_window_name, text="发送的消息请求")
        self.result_data_label.grid(row=0, column=22)
        self.result_data_label1 = Label(self.init_window_name, text="获取的返回值")
        self.result_data_label1.grid(row=12, column=22)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)
        #文本框
        self.init_data_Text = Text(self.init_window_name, width=45, height=20)  #原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=60,height=20)  #处理结果展示
        self.result_data_Text.grid(row=1, column=22, rowspan=10, columnspan=10)

        self.result_data_Text1 = Text(self.init_window_name, width=60,height=20)  #处理结果展示
        self.result_data_Text1.grid(row=13, column=22, rowspan=10, columnspan=10)

        self.log_data_Text = Text(self.init_window_name, width=45, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        #按钮
        self.str_trans_to_md5_button = ttk.Button(self.init_window_name, text="生成参数", width='5',command=self.getMessage)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=1, column=11,columnspan=10)
        self.str_trans_to_md5_button1 = ttk.Button(self.init_window_name, text="生成用例", width='5',command=self.createTestCase)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button1.grid(row=2, column=11,columnspan=10)

        #tree
        

    #功能函数
    def getMessage(self):
        # src = self.init_data_Text.get(1.0,END).strip().replace("\n","").encode()
        src = self.init_data_Text.get(1.0,END)
        #print("src =",src)
        if src:
            try:
                jstr=json.loads(src)
                request_str=jstr['log']['entries'][0]['request']
                respone_str=jstr['log']['entries'][0]['response']
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,json.dumps(request_str, sort_keys=True, indent=4, separators=(',', ': ')))
                self.result_data_Text1.delete(1.0,END)
                self.result_data_Text1.insert(1.0,json.dumps(respone_str, sort_keys=True, indent=4, separators=(',', ': ')))
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

    def createTestCase(self):
        req_str=json.loads(self.result_data_Text.get(1.0,END))
        res_str=json.loads(self.result_data_Text1.get(1.0,END))
        # print(req_str)
        urldata=req_str['url'].split('/')[3:]
        newrul='/'.join(str(i) for i in urldata)
        req_str['url']=newrul
        # print(req_str)
        self.write_log_to_Text("获取API接口：{0}".format(newrul))
        modelpath="../testdata/model/"
        casepath="../testcase/"
        modelname=newrul.replace('/','_')[:-1]
        self.writeFile(modelpath+modelname+'_model.json',json.dumps(req_str, sort_keys=True, indent=4, separators=(',', ': ')))
        self.writeFile(modelpath+modelname+'_rep.json',json.dumps(res_str, sort_keys=True, indent=4, separators=(',', ': ')))

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


