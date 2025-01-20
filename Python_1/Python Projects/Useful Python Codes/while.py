"""
# print 1 to 10
i=1
while(i<=10):
    print(i)
    i=i+1
    
# print 10 20 30 40 50
i=10
while(i<=50):
    print(i)
    i=i+10
# 8 7 6 5 4 3 2
i=8
while(i>=2):
    print(i)
    i=i-1
    
#1+2+3+..10
i=1
s=0
while(i<=10):
    s=s+i
    i=i+1
print(s)


#calcuating the value of a certain amount of digits total value Ex: 369=3+6+9=18
n=(int(input('Give me a number')))
d=n
rev=0
while(n!=0):
    rem=n%10
    rev=rem+rev*10
    n=n//10
print('{} is reversed it is {}'.format(d,rev))


#write a python program that takes a number ,reverse it and if the reverse and the number is same print palindrome else not a palindrome


n=(int(input('Give me a number')))
j=n
s=0
while (n!=0):
   rem=n%10
   s=s*10+rem
   n=n//10
print(s)

if (j==s):
    print('your number is a palindrome')
elif (j!=s):
    print('your number is not a palindrome 
    
n=(int(input('give me a number')))
j=n
s=0
while(n!=0):
    rem=n%10
    s=s+(rem*rem*rem)
    n=n//10
print(s)

if(j==s):
    print('The numbers {} and {} are armstorngs'.format(j,s))
else:
    print('Your numbers {} and {} are not armstrongs an armstrong for example is 153 try again. '.format(j,s))

j=int(input('Give me a number'))
a=0
b=1
print(a)
print(b)
for i in range(j-2):
    c=a+b
    print(c)
    a=b
    b=c
    
#2*4*6*8*10
i=2
s=1
while(i<=10):
    s=s*i
    i=i+2


i=1
s=int(input('Give me a number'))
n=1
while (i<=s):
    n=n*i
    i=i+1
print(n)    
"""

