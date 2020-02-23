# _*_ coding:utf-8 _*_

import tkinter
from tkinter import filedialog

def openfiles2():
    s2fname = filedialog.askopenfilename(title='打开S2文件', filetypes=[('S2out', '*.jpeg'), ('All Files', '*')])
    print(s2fname)
    print(type(s2fname))
    print(dir(s2fname))
def openfilecgns():
    cgnsfname = filedialog.askopenfilename(title='打开CGNS文件',filetypes=[('CGNSdat', '*.dat'), ('All Files', '*')] )
    print(cgnsfname)
 
root = tkinter.Tk()
#root.geometry('500x300+500+200')
btn1 = tkinter.Button(root, text='打开S2文件',font =("宋体",20,'bold'),width=13,height=8, command=openfiles2)
btn2 = tkinter.Button(root, text='打开CGNS文件',font = ('宋体',20,'bold'),width=13,height=8, command=openfilecgns)
 
btn1.pack(side='left')
btn2.pack(side='left')
root.mainloop()