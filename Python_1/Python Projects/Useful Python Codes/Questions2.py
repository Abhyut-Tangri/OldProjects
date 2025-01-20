"""
from msilib.schema import ListBox
from tkinter import *
def insertion():
    cur=sp.curselection()
    for i in cur:
        ssp2.insert(END,sp.get(i))
def deletion():
    curse=sp.curselection()
    for i in curse:
        sp.delete(i)
def deletions():
    curse=ssp2.curselection()
    for i in curse:
        ssp2.delete(i)
tk=Tk()
sp=Listbox(tk,selectmode=MULTIPLE)
sp.insert(1,'USA')
sp.insert(2,'CANADA')
sp.insert(3,'INDIA')
sp.insert(4,'JAPAN')
sp.pack()
ssp2=Listbox(tk)
ssp2.pack()
add=Button(tk,text='Add',command=insertion)
delete=Button(tk,text='Delete',command=deletion)
deletes=Button(tk,text='Delete',command=deletions)
add.pack()
delete.pack()
tk.mainloop()



for i in range(5,0,-1):
    for k in range(3-i,0,-1):
        print(' ' ,end='')
    for j in range(1,i+1):
        print('* ' ,end='')
    print()

a=')'
for i in range(1,5):
    for k in range(5-i,0,-1):
        print(' ',end='')
    for f in range(1,i+1):
        if a==')':
            a='('
        else:
            a=')'
        print(a,end='')
    print()

for i in range(1,5):
    for k in range(4-i,0,-1):
        print(' ' ,end='')
    for j in range(1,i+1):
        print('O ' ,end='')
    print()
for i in range(3,0,-1):
    for k in range(4-i,0,-1):
        print(' ' ,end='')
    for j in range(1,i+1):
        print('O ' ,end='')
    print()

for i in range (1,11):
    for j in range(1,11):
        if j==1 or j==10 or i==1 or i==10:
            print('.',end='')
        else:
            print(' ',end='')

    print()
"""
from tkinter import *  
  
top = Tk()  
sb = Scrollbar(top)  
sa=Scrollbar(top)
sb.pack(side = RIGHT, fill = Y)  
  
mylist = Listbox(top, yscrollcommand = sb.set,xscrollcommand=sa.set )  

for line in range(30):  
    mylist.insert(END, "Number " + str(line))  
  
mylist.pack( side = LEFT )  
sa.pack(fill=X)
mainloop()
