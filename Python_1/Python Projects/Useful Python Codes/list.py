"""
a=input('give me a wrod/letter/sentence')
b='aeiou'
for x in a:
    if x not in b:
        print(x)

print('The amount vowels was {} and consanants was {}'.format(v,c))



a=input('give me a word/letter/sentence')
b=a[::-1]
print(b)

if(a==b):
    print('{} and {} are palindromes'.format(b,a))
else:
    print('{} and {} are not palidromes'.format(b,a))
 
#write a python program that takes the username and password from the user and if the username iand the password both is admin print welcome admin otherwise you have to sa invalid user
AdminUser='Abhyut_Tangri'
AdminPassword='123456'
Username=input('Give your username here')
Password=input('Give password here')
if(AdminUser==Username and AdminPassword==Password):
    print('Welcome Abhyut_Tangri')
else:
    print('Your username:{} and password {} are invalid; Please try again'.format(Username,Password))


#write a python program to find the number of words from the input user has entered
a=input('give me a word/letter/sentence')
b=' '
s=0
c=0
for x in a:
    if x in b:
        s=s+1
        c=s+1 
    else:
        pass

print('You have {} words'.format(c))


#write a python program that accept a word from the user and captalize all letters whics are vowel
word=input('Give me a word')
b='aeiou'

for x in word:
    if x in b:
        print(x.upper())
    else:
        print(x.lower())


a=[1,2,3,4,5,6,7,"hello",5,3,2,8]

a.append(33)
a.insert(3,3.5)
a[3]=3.7
a.pop(3)
print(a)
a.remove("hello")
a.sort()
b=[99,88,77]
c=a+b
print(c)


l=[4,5,6,7]
c=l*3
print(c)

a=[]

b=eval(input('How many values would you like to insert into the list?'))
for i in range(b):
    c=eval(input('What values would you like to enter'))
    a.append(c)
print(a)
while(True):
    choose=int(input('Choose 1 for insert,2 for appending, and 3 for deleting with index,4 for deleting with item name'))
    if(choose==1):
        l=int(input('Where would you like to insert your value, remember to choose between 0-how many values you have?'))
        d=int(input('What would you like to insert?'))
        a.insert(l,d)
    elif(choose==2):
        l=int(input('What is the value that is bieng appended?'))
        a.append(l)
    elif(choose==3):
        l=int(input('What is the index of the deleted value?'))
        a.pop(l)
    elif(choose==4):
        l=eval(input('What is the name of the value that is bieng deleted'))
        a.remove(l)
    else:
        print('{} is not valid'.format(choose))
    print(a)
    cont=int(input('press 1 to continue anything else will stop'))
    if(cont!=1):
       break


a=[]
b=eval(input('How many values would you like to insert into the list?'))
for i in range(b):
    c=eval(input('What values would you like to enter'))
    if(c>0):    
        a.append(c)
        
a.sort()
print(a)
  

a=[]
b=eval(input('How many values would you like to insert into the list?'))
for i in range(b):
    c=eval(input('What values would you like to enter'))
    a.append(c)
 

min=int(input('Give me a minimum value'))
max=int(input('Give me a maximum value'))
for i in a:
    if(i>=min and i<=max):   
        print(i)

             
highway=int(input('Give me a highway number'))
if(highway<100 and highway>=1 ):
    if(highway%2==0):
        print('Your primary highway is going east/west')
    else:
        print('your primary highway is going north/south')
elif(highway>=100 and highway<=999):
    highway=highway%100
    if(highway%2==0):
        print('Your auxillary  highway serves I-{},going east/west'.format(highway))
    else:
        print('your auxillary highway serves I-{},going north/south'.format(highway))
else:
    print('{} is not valid highway'.format(highway))

t=(3,5,6,7,8)
print(type(t))
for i in t:
    if(i%2==0):
        print(i)

t=(1,4,3)
l=list(t)
l[1]=5
t=tuple(l)
print(t)  
print(len(t))      

t=(1,2,3,4,5)
c=int(input('What value would you like to add'))
l=list(t)
l.append(c)
t=tuple(l)    
print(t)


Counts the number of occurrences of item 50 from a tuple
Given:

tuple1 = (50, 10, 60, 70, 50)
Expected output:

2

 Swap two tuples in Python
Given:

tuple1 = (11, 22)
tuple2 = (99, 88)
Expected output:
tuple1: (99, 88)
tuple2: (11, 22)

Copy specific elements from one tuple to a new tuple
Write a program to copy elements 44 and 55 from the following tuple into a new tuple.

Expected output:

tuple2: (44, 55)


    
tuple1 = (11, 22, 33, 44, 55, 66)
list1=list(tuple1)
list1.remove(11)
list1.remove(22)
list1.remove(33)
list1.remove(66)
tuple1=tuple(list1)
print(tuple1)

tuple1=(11,22)
tuple2=(99,88)
list1=list(tuple1)   
list2=list(tuple2)
list1.remove(22)
list1.remove(11)
list2.remove(99)
list2.remove(88)
list1.append(99)
list1.append(88)
list2.append(11)
list2.append(22)
tuple1=tuple(list1)
tuple2=tuple(list2)
print(tuple1)
print(tuple2)

tuple1=(50, 10, 60, 70, 50,50)
print(tuple1.count(50))

tuple1=(11,22)
tuple2=(99,88)
list1=list(tuple1)   
list2=list(tuple2)
list1.remove(22)
list1.remove(11)
list2.remove(99)
list2.remove(88)
list1.append(99)
list1.append(88)
list2.append(11)
list2.append(22)
tuple1=tuple(list1)
tuple2=tuple(list2)
print(tuple1)
print(tuple2) 
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2=()
list1=list(tuple2)
list1.append(44)
list1.append(55)
tuple2=tuple(list1)
print(tuple2)
"""

