from tkinter import * 
from tkinter.ttk import * 
from time import strftime
from termcolor import colored

# creating tkinter window
root = Tk()
root.title('Menu Demonstration')
  
# Creating Menubar
menubar = Menu(root)
""" 
# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)

file.add_command(label ='New File', command = None)
file.add_command(label ='Open...', command = None)
pdfword=Menu(file,tearoff=0)
pdfword.add_command(label='PDF')
pdfword.add_command(label='WORD')
file.add_cascade(label ='Save', menu=pdfword)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)

e=Menu(menubar,tearoff=0)
e.add_command(label='Cut')
candp=Menu(e,tearoff=0)
candp.add_command(label='Select')
candp.add_command(label='Select All')
e.add_cascade(label='Copy',menu=candp)
e.add_command(label='Paste')
e.add_command(label='Select All')
e.add_separator()
e.add_command(label='Find...')
e.add_command(label='Find Again')

help=Menu(menubar,tearoff=0)
help.add_command(label='Tk Help')
help.add_command(label='Demo')
help.add_separator()
help.add_command(label='About Tk')

menubar.add_cascade(label ='File', menu = file)
menubar.add_cascade(label='Edit',menu=e)
menubar.add_cascade(label='Help',menu=help)
"""
def red():
    a.configure(foreground='red')
def blue():
    a.configure(foreground='blue')
def green():
    a.configure(foreground='green')
color=Menu(menubar,tearoff=0)
color.add_command(label='Red',command=red)
color.add_command(label='Blue',command=blue)
color.add_command(label='Green',command=green)
menubar.add_cascade(label='Colors',menu=color)
a1=Label(text='Color Changer')
a =Entry()
a1.pack()
a.pack()
a.config
()
root.config(menu = menubar)
mainloop()
