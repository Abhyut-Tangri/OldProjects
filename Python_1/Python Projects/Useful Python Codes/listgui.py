from msilib.schema import ListBox
from tkinter import *
m=Tk()
def deleter():
    j=Lb1.curselection()
    for i in j:
        Lb1.delete(i)
def adder():
    r=Lb1.curselection()
    for i in r:
        l.insert(END,Lb1.get(i))
Lb1=Listbox(m,selectmode=MULTIPLE)
Lb1.insert(1,'Apple')
Lb1.insert(2,'Mango')
Lb1.insert(3,'Strawberry')
Lb1.insert(4,'Peach')
Lb1.insert(5,'Cherry')
Lb1.pack()
delete=Button(m,text='Delete',command=deleter)
add=Button(m,text='Add',command=adder)
l=Listbox(m)
delete.pack()
add.pack()

l.pack()
m.mainloop()