from tkinter import *
import tkinter as tk
m=tk.Tk()
m.geometry('1500x1500') 
l=[(1,2,3,4,5,6,7),('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'),('Something','Something','Something','Something','Something','Something','Something')]
for x in range (3):
    for y in range(7):
        t=Text(m,width=20,height=20)
        t.grid(row=x,column=y)
        t.insert(END,l[x][y])
        t.config(state='disabled')
m.mainloop()