from tkinter import *
from turtle import radians
m=Tk()
"""
def liste(event):
    r=listes.curselection()
    for i  in r:
        if(i==0):
            m.configure(background='red')
listes=Listbox(m)
listes.insert(0,'Red')
listes.insert(1,'Blue')
listes.insert(2,'Green')
listes.insert(3,'Yellow')
listes.insert(4,'Grey')
lab=Label(m,text='Default')
listes.bind('<Double-1>',liste)
m.geometry('500x500')
listes.pack()
lab.pack()


create a empty listbox, a textbox and two buttons add and delete. on click of the add button take the content from text box and insert it to the listbox. on click of the delete button delete the item from the listbox

"""
def deleter():
    j=lists.curselection()
    for i in j:
        lists.delete(i)

def adder():
    i=1
    r=a1.get()
    lists.insert(END,r)
lists=Listbox(m)
a=Label(m, text="What is bieng put in")
a1=Entry(m)
delete=Button(m,text='Delete',command=deleter)
aDd=Button(m,text='Add',command=adder)
lists.pack()
a.pack()
a1.pack()
delete.pack()
aDd.pack()

m.mainloop()