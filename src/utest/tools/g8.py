import tkinter
from tkinter import ttk

root = tkinter.Tk()

tree = ttk.Treeview(root, show="headings", columns=('col1','col2','col3'))


tree.heading('col1', text='第一列')

tree.heading('col2', text='第二列')

tree.heading('col3', text='第三列')

tree.column('col1', width=100, anchor='center')

tree.column('col2', width=100, anchor='center')

tree.column('col3', width=100, anchor='center')


def onDBClick(event):

    item = tree.selection()[0]

    print (("you clicked on "), tree.item(item, "values"))


for i in range(10):

    tree.insert('',i,values=('a'+str(i),'b'+str(i),'c'+str(i)))

tree.bind("<Double-1>", onDBClick)

tree.pack()

root.mainloop()