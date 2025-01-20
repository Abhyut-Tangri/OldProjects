
from tkinter import *
from tkinter import colorchooser
import tkinter as tk
import tkinter as tk

def hide():
    text.tag_add("hidden", "sel.first", "sel.last")

def show_all():
    text.tag_remove("hidden", "1.0", "end")

root = tk.Tk()
toolbar = tk.Frame(root)
hide_button = tk.Button(toolbar, text="Hide selected text", command=hide)
show_button = tk.Button(toolbar, text="Show all", command=show_all)
hide_button.pack(side="left")
show_button.pack(side="left")

text = tk.Text(root)
text.tag_configure("hidden", elide=True, background="red")



toolbar.pack(side="top", fill="x")
text.pack(side="top", fill="both", expand=True)

text.tag_add("sel", "3.0", "8.0")
root.mainloop()
'''
#CHeck if number is lucky or not, but gui
m.geometry('500x500')
def lucky():
    n=int(numbers.get())
    while(n>9):
        sum=0
        while(n!=0):
            rem=n%10
            sum=sum+rem
            n=n//10
        n=sum
    if n==1:
        print('Your number is indeed lucky')
    else:
        print ('Get a better number')

numbers=Entry(m,width=50, font=('Arial 20'))
check=Button(m,text='Check for lucky number',command=lucky)
numbers.place(anchor=CENTER)
check.pack()
color=colorchooser.askcolor()
c=color[1]
m.configure(background=c)

m.geometry('300x200')
def reversed():
    reversing = str(reverse.get())[::-1]
    output.insert(END,reversing)
def UpLoW():
    Ups= str(reverse.get())
    print("Capital Letters: ", sum(1 for c in Ups if c.isupper()))
    print("Lowercase Letters: ", sum(1 for c in Ups if c.islower()))
reverse=Entry(m,width=50, font=('Arial 20'))
output=Entry(m,width=50, font=('Arial 20'))
output.config(state='disabled')
rev=Button(m,text='REVERSE',command=reversed)
uplow=Button(m,text='Upper & Lower',command=UpLoW)
reverse.pack(padx=15,pady=15)
output.pack()
rev.pack()
uplow.pack(padx=15,pady=15)

m.mainloop()
'''
