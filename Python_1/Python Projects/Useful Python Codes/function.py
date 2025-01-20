"""
def add(a,b):

    print(a+b)
    
x=int(input("enter number"))
y=int(input("enter number"))
add(x,y)

def cube(a):
    print(a*a*a)

x=int(input('Enter number'))
cube(x )


write a python program that defines a function for finding whether the number is positive or negative
def find(a):
    if a>0:
        print('{} is postive'.format(a))
    elif a<0:
        print('{} is negative'.format(a))
    else:
        print('{} is not a valid number'.format(a))
x=int(input('Give me a number'))
find(x)
    
write a function that will find the addition subtraction multiplication and division of 2 number
def all(a,b):
    print(a-b)
    print(a+b)
    print(a*b)
    print(a/b)
x=int(input('give me a number'))
y=int(input('Give me a number'))
all(x,y)
    
"""
def add(a,b):
    print(a+b)
def sub(a,b):    
    print(a-b)
def mult(a,b):    
    print(a*b)
def div(a,b):
    print(a/b)
x=int(input('give me a number'))
y=int(input('Give me a number'))
menu=int(input('Choose one for adding, 2 for subtraction,3 multipication,4 is division'))
if menu==1:
    add(x,y)
elif menu==2:
    sub(x,y)
elif menu==3:
    mult(x,y)
elif menu==4:
    div(x,y)
else:
    print('{} is not one of the allowed math things'.format(menu))
 
