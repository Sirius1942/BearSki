# -*- encoding: utf-8 -*-
'''
@File    :   ApiTestGui.py
@Time    :   2020/02/02 16:05:17
@Author  :   chenjiusi 
'''

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import hashlib
import time
import json
from BearSki.utils.hartool import HarTool
import sys
import time
import threading
LOG_LINE_NUM = 0

class ApiTest_GUI(): 
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

        self.HarTool= None



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
        self.har_path_input2=Entry(self.init_window_name,width=15)
        self.har_path_input2.grid(row=self.row_1,column=self.column_row1_3,sticky=N+E,padx=self.pdx,pady=self.pady)

        self.put_one_request = ttk.Button(self.init_window_name, text="生成用例",command=self.createOneCase)  # 调用内部方法  加()为直接调用
        self.put_one_request.grid(row=self.row_1, column=self.column_row1_4,sticky=N+W,padx=self.pdx,pady=self.pady)
        self.put_all_request = ttk.Button(self.init_window_name, text="批量生成用例",command=self.createAllCase)  # 调用内部方法加()为直接调用
        self.put_all_request.grid(row=self.row_1, column=self.column_row1_5,sticky=N+W,padx=self.pdx,pady=self.pady)
        # self.put_all_request = ttk.Button(self.init_window_name, text="测试退出",command=self.win_exit)  # 调用内部方法加()为直接调用
        # self.put_all_request.grid(row=self.row_1, column=self.column_row1_5,sticky=N+W,padx=self.pdx,pady=self.pady)

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
        self.init_window_name.bind("<Control-d>", self.win_exit)

    def onDBClick(self,event):
        try:
            item = self.init_tree.selection()[0]
            modelname=self.init_tree.item(item, "values")
            print ("you clicked on name is :{0} ".format(modelname[0]))
            self.getOneMessage(modelname[0])
            self.write_log_to_Text("INFO: 查看接口 【{0}】的信息".format(modelname[0]))
            self.har_path_input2.insert(0,modelname[0])
        except Exception as e:
            self.write_log_to_Text("ERROR: {0}".format(e))
        
    
    def openfiles(self):
      try:
            harfilename = filedialog.askopenfilename(title='打开Har文件', filetypes=[('har', '*.har'), ('All Files', '*')],initialdir='./')
            self.har_path_input.insert(0,harfilename)
            self.write_log_to_Text("INFO: 打开文件: {0}".format(harfilename))
            self.HarTool=HarTool(harfilename)
            #清空表格
            table_items=self.init_tree.get_children()
            for item in table_items:
                self.init_tree.delete(item)
            i=0
            for name in self.HarTool.harfile.keys():
                self.init_tree.insert('',i,values=(name))
      except Exception as e:
            self.write_log_to_Text("ERROR: {0}".format(e))
      

    def getOneMessage(self,name):
        try:
            self.write_log_to_Text("INFO: 获取一条返回值模型信息")
            result,res=self.HarTool.getMessage(name)
            self.result_data_Text.delete(1.0,END)
            self.result_data_Text.insert(1.0,json.dumps(result, sort_keys=True, indent=4, separators=(',', ': '),ensure_ascii=False))
            self.result_data_Text1.delete(1.0,END)
            self.result_data_Text1.insert(1.0,json.dumps(res, sort_keys=True, indent=4, separators=(',', ': '),ensure_ascii=False))
    
        except Exception as e:
            self.write_log_to_Text("ERROR: {0}".format(e))
        
    def createAllCase(self):
        try:
            self.write_log_to_Text("INFO: 开始为全部接口信息创建测试用例")
            self.HarTool.createALLCase()
            self.write_log_to_Text("INFO: 全部用例创建结束")
        except Exception as e:
            self.write_log_to_Text("ERROR: {0}".format(e))

    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time
    
    def createOneCase(self):
        try:
            req_str=json.loads(self.result_data_Text.get(1.0,END))
            self.write_log_to_Text("INFO: 开始生成单条测试用例 {0}".format(req_str['name']))
            res_str=json.loads(self.result_data_Text1.get(1.0,END))
            self.HarTool.createTestCase(req_str,res_str)
            self.write_log_to_Text("INFO: 成功生成用例")
        except Exception as e:
            self.write_log_to_Text("ERROR: {0}".format(e))
        
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
    
    def win_exit(self,event):
        print("in exit")
        self.init_window_name.destroy()

def gui_start(mode):
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = ApiTest_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()
    print("guitools startup ...")
    if mode == "test":
        init_window.mainloop(2)
    else:
        init_window.mainloop()
    # # ZMJ_PORTAL.initData()
    # init_window.mainloop(3)          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示
    print("guitools exit.")


# if __name__ == "__main__":

#     gui_start()
