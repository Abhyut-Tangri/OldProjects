"""
while(True):
    n=int(input('give me a number'))
    j=n%2
    if (j==
        print('Your number is even')
    else:
        print('Your number is odd')
    cont=input('Press y to continue please do lowerCASE')
    if (cont!='y'):
        break

while(True):
    a=int(input('Give me a number'))
    b=int(input('Give me a number'))
    print(' Choose between 1 (addition), 2 subtarction, 3 division, 4 multipication')    
    th=int(input('Choose between 1,2,3,or 4'))
    if (th==1):
        print(a+b)
    elif(th==2):
        print(a-b)
    elif(th==3):
        print(a/b)
    elif (th==4):
        print(a*b)
    else:
        print(' your number of {} is not 1 2 3 or 4 try again'.format(th))
    l=input('type l if you would like to stop anything else will continue')
    if (l=='l'):
        break

write a python program that takes age from 
from the user and if the age is negative askthe age again until user gives a positive number otherwise display your age is whatever
take 2 numbers from the user and print greater number infinity times until user enters a negative number in any of the two numbers
oupput
enter number 8
enter number 2
8 is greate
enter number 5
enter number 19
19 is GREATERenter number -7
enter number 9

while(True):
    age=int(input('What is your age'))
    if (age >=0):
        break
    else:
        print('your age of {} is not valid'.format(age))
print('Your age is {}'.format(age))
"""    
while(True):
    num1=int(input('Give me the first number to compare'))
    num2=int(input('Give me another number'))
    if (num1 < 0 or num2 < 0):
        break 
    if(num1>num2):
        print('{}>{}'.format(num1,num2))
    elif(num1==num2):
        print('Your numbers {} and {} are equal'.format(num1,num2))
    else:
        print('{}>{}'.format(num2,num1))   