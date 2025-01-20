from tkinter import *
import tkinter as tk
m=tk.Tk()
expression = ""
 
 

def press(num):

    global expression
    expression = expression + str(num)
    v.set(expression)
def equalpress():
      global expression
      t=str(eval(expression))
      v.set(t)
      expression=""  
      
def cleared():
        global expression
        expression=''
        v.set(expression)
      
 
        
m.title('Calculator')
m.configure(background='black') 
   
m.geometry('550x510')
v=StringVar()
e=Entry(m,textvariable=v,)
e.grid(columnspan=4,ipadx=215)

b=Button(m,text='1',fg='black',bg='white',
        command=lambda: press(1),height=3,width=7,)
b.grid(row=1,column=0,ipadx=39)
b1=Button(m,text='2',fg='black',bg='white',
          command=lambda: press(2), height=3,width=7)
b1.grid(row=1,column=1,ipadx=39)
b2=Button(m,text='3',fg='black',bg='white',
        command=lambda: press(3),height=3,width=7)
b2.grid(row=1,column=2,ipadx=39)
b3=Button(m,text='4',fg='black',bg='white',
        command=lambda: press(4),height=3,width=7)
b3.grid(row=1,column=3,ipadx=39)
b4=Button(m,text='5',fg='black',bg='white',
        command=lambda: press(5),height=3,width=7)
b4.grid(row=2,column=0,ipadx=39)
b5=Button(m,text='6',fg='black',bg='white',
        command=lambda: press(6),height=3,width=7)
b5.grid(row=2,column=1,ipadx=39)
b6=Button(m,text='7',fg='black',bg='white',
        command=lambda: press(7),height=3,width=7)
b6.grid(row=2,column=2,ipadx=39)
b7=Button(m,text='8',fg='black',bg='white',
        command=lambda: press(8),height=3,width=7)
b7.grid(row=2,column=3,ipadx=39)
b8=Button(m,text='9',fg='black',bg='white',
        command=lambda: press(9),height=3,width=7)
b8.grid(row=3,column=0,ipadx=39)
b9=Button(m,text='0',fg='black',bg='white',
        command=lambda: press(0),height=3,width=7)
b9.grid(row=3,column=1,ipadx=39)
equal=Button(m,text='=',fg='black',bg='white',command=lambda:equalpress(),height=3,width=7)
equal.grid(row=3,column=2,ipadx=39)
clear=Button(m,text='CLEAR',fg='black',bg='white',command=lambda:cleared(),height=3,width=7)
clear.grid(row=3,column=3,ipadx=39)
plus=Button(m,text='+',fg='black',bg='white',
        command=lambda: press('+'),height=3,width=7)
plus.grid(row=4,column=0,ipadx=39)
minus=Button(m,text='-',fg='black',bg='white',
        command=lambda: press('-'),height=3,width=7)
minus.grid(row=4,column=1,ipadx=39)
division=Button(m,text='/',fg='black',bg='white',
        command=lambda: press('/'),height=3,width=7)
division.grid(row=4,column=2,ipadx=39)
multiply=Button(m,text='*',fg='black',bg='white',
        command=lambda: press('*'),height=3,width=7)
multiply.grid(row=4,column=3,ipadx=39)
equal.grid(row=3,column=2,ipadx=39)
intro=Button(m,text='intro',fg='black',bg='white',
        command=lambda: press('Hi this is my calculator, press the buttons to create and equation + to add - subtraction, / for division and * for multipication!'),height=3,width=7)
intro.grid(row=5,column=0,ipadx=39)
m.mainloop()