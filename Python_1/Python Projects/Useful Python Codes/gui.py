import math
from textwrap import dedent
import tkinter as tk
from tkinter import BOTTOM, LEFT, RIGHT, messagebox 
m=tk.Tk()
def squareroot():
    f=1
    a=int(no1.get())
    messagebox.showinfo("Root",math.sqrt(a))
    print(f)
no1=tk.Entry()
a=tk.Button(m,text='Square Root',command=squareroot)
no1.pack()
a.pack()
"""
m.geometry('500x500')
def factorial():
    f=1
    a=int(no1.get())
    for i in range(1,a+1):
        f=f*i
    print(f)
def reverse():
    a=int(no1.get())
    j=a
    s=0
    while (a!=0):
        rem=a%10
        s=s*10+rem
        a=a//10
    print(s)
l=tk.Label(m,text='Enter number here')
no1=tk.Entry()

a=tk.Button(m,text='Factorial',command=factorial)
b=tk.Button(m,text='Reverse',command=reverse)

l.pack(side=LEFT)
no1.pack(side=LEFT)
a.pack(side=BOTTOM)
b.pack(side=RIGHT)

def add():
    p=int(no1.get())
    q=int(no2.get()    )
    messagebox.showinfo("Addition",p+q)

def sub():    
    p=int(no1.get())
    q=int(no2.get()    )
    messagebox.showinfo("Subtraction",p-q)
def mult():    
    p=int(no1.get())
    q=int(no2.get()    )
    messagebox.showinfo("Multipication",p*q)
def div():
    p=int(no1.get())
    q=int(no2.get()    )
    messagebox.showinfo("Division",p/q)
l=tk.Label(m,text='Enter Number 1 here')
no1=tk.Entry()
ce=tk.Label(m,text='Enter Number 2 here')
no2=tk.Entry()

a=tk.Button(m,text='Add',command=add)
b=tk.Button(m,text='Subtract',command=sub)
c=tk.Button(m,text='Multiply',command=mult)
d=tk.Button(m,text='Divide',command=div)
l.pack()
no1.pack()
ce.pack()
no2.pack()
a.pack()
b.pack()
c.pack()
d.pack()
"""
m.mainloop()
"""
CREAte a gui program for finding factorial and reverse of a number using functions


"""


