from select import select
from statistics import variance
from tkinter import *
m=Tk()

def armstrong():
    b=int(a1.get())
    j=b
    s=0
    while(b!=0):
        rem=b%10
        s=s+(rem*rem*rem)
        b=b//10
    print(s)

    if(j==s):
        print('The numbers {} and {} are armstorngs'.format(j,s))
    else:
        print('Your numbers {} and {} are not armstrongs an armstrong for example is 153 try again. '.format(j,s))
p=IntVar()
a=Label(m,text='Number to be Checked')
a1=Entry(m)
arm1=Button(m,text='Armstrong',command=armstrong)
a.pack()
a1.pack()
arm1.pack()
"""
def submission():
    a=name1.get()
    b=p.get()
    d=int(age1.get)
    if d>18:
        messagebox.showinfo("Hi {}.{} you are eligible to vote at your current age of {}".format(b,a,d))
    elif 0<d<18:
        messagebox.showinfo("Hi {}.{} you are not able vote at your current age of {}".format(b,a,d))
    else:
        messagebox.showinfo("Hi {}.{} your given value age of {} is not valid please try putting in a postivie number thank you".format(b,a,d))
p=IntVar()
name=Label(m,text="Name").grid(row=0,column=0)
name1=Entry(m)
name1.grid(row=0,column=1,sticky=W)
Male=Radiobutton(m,text="Male",variable=p,value='Mr').grid(row=1,column=1,sticky=W)
Female=Radiobutton(m,text="Female",variable=p,value='Ms').grid(row=2,column=1,sticky=W)
age=Label(m,text="Age").grid(row=3,column=0,sticky=W)
age1=Entry(m,sticky=W)
age1.grid(row=3,column=1,sticky=W)
submit=Button(m,text="Submit",command=submission).grid(row=4, column=0,sticky=W)


def bill():
    bin=int(p.get())*int(quantity.get())
    mpty.config(text=bin)
p=IntVar()
fruit=Label(m, text='Fruit')
Apple=Radiobutton(m,text='Apple Juice',variable=p,value=5)
Mango=Radiobutton(m,text='Mango Juice',variable=p,value=10)
Orange=Radiobutton(m,text='Orange Juice',variable=p,value=7)
q=Label(m,text='Quantity')
quantity=Entry(m)
bill=Button(m,text='Bill',command=bill)
fruit.pack()
Apple.pack()
Mango.pack()
Orange.pack()
q.pack(side=LEFT)
quantity.pack(side=LEFT)
bill.pack(anchor=W)
mpty=Label(m)
mpty.pack()


def sel():
    select=str(a.get())
    l.config(text=select)
a=StringVar()
red=Radiobutton(m,text='Red',variable=a,value='Red',command=sel)
blue=Radiobutton(m,text='Blue',variable=a,value='Blue',command=sel)
green=Radiobutton(m,text='Green',variable=a,value='Green',command=sel)
l=Label(m)
red.pack(anchor=W)
blue.pack(anchor=W)
green.pack(anchor=W)
l.pack()
"""
m.mainloop()