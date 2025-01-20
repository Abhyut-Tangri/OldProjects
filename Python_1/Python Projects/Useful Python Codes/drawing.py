
from tkinter import *
import MySQLdb


root = Tk()
 
C = Canvas(root, bg="white",
           height=674, width=574)
""" 
line = C.create_line(108, 57,
                     40, 148,
                     fill="green")
l = C.create_line(108, 57,
                     173,155,
                     fill="green")
li = C.create_line(40, 148,173,155,fill="green")
O=C.create_oval(92,100,128,141)
arc = C.create_arc(180, 150, 80,
                   210, start=0,
                   extent=220,
                   fill="red")
C.pack()
"""
c=C.create_oval(58,44,568,348,fill="brown")
d=C.create_oval(166,79,261,138,fill="blue")
e=C.create_oval(323,80,423,132,fill="blue")
a=C.create_line(287,139,287,219,fill="green")
b=C.create_oval(186,244,424,293,fill="red")
C.pack()
mainloop()

