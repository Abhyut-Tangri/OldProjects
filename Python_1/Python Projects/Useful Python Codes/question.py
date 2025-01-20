"""
#Program to find square and cube of a number
a=eval(input("Give me a number"))
b= a*a
print('Square of {} is {}'.format(a,b))
c=a**3
print('The cube of {} is {}'.format(a,c))

#Program to find area of circle
r=eval(input('Give me a number'))
a=r*r*3.14
print(a)

#Program that accept 5 subject marks from user and print the total and percentage .
e=eval(input('Mark for english'))
m=eval(input('What is your mark for math'))
s=eval(input('What is your mark for science'))
h=eval(input('What is your mark for history'))
sp=eval(input('What is your mark for spanish'))
t=(e+m+s+h+sp)
p=t/250*100
print('The total marks is {} and the average mark is {}'.format(t,p))




#Program that find the simple interest 
p=eval(input('What is your principal value?'))
r=eval(input('What is your rate value?'))
t=eval(input('Over how much time is your intrest bieng calculated?'))
i=p*r*t/100
print(i)
"""

#Program to find area of triangle
b=eval(input('Give me a number for the base of your triangle '))
h=eval(input('Give me a number for the height of your triangle '))
a=b*h/2
print(a)