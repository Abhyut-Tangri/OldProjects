"""
x=int(input('please give me a number'))
sum=0
c=x
if c==0:
    print('Make this harder on me')
elif c==1:
    print('Too easy')
while (x!=0):
    rem=x%10
    sum=sum+(rem*rem*rem)
    x=x//10

if sum==c:
    print('Your number is a armstrong')
else:
    print('Your number is not a armstrong try again')

take a number from user and check if prime or not

Write a program to display the output in the following format. (Using Nested Loops)
5
45
345
2345
12345
Write a program to accept a number (not constant) then check the number is perfect number or not.

prime=input('Give me a number')
flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, prime):
        if (prime % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(prime, "is not a prime number")
else:
    print(prime, "is a prime number")

for i in range(5,1):
    for l in range(i,1):
        print(l,end=' ')
    
n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")

prime=int(input('Give me a number'))
flag = False

# prime numbers are greater than 1
if prime > 1:
    # check for factors
    for i in range(2, prime):
        if (prime % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(prime, "is not a prime number")
else:
    print(prime, "is a prime number")

for i in range (100,1000):
    c=i
    s=0
    while i!=0:
        rem=i%10
        s=s+(rem*rem*rem)
        i=i//10
    if c==s:
        print(c) 

for i in range(1,50):
    p=i
    flag=False
    for c in range(2,i):
        if (i%c==0):
            flag=True
            break
    if flag:
        pass
    else:
        print(p)

n=int(input('Gie me a lucky number'))
while(n>9):
    sum=0
    while(n!=0):
        rem=n%10
        sum=sum+rem
        n=n//10
    n=sum
if n==1:
    print('Your number is indeed lucky')
else:
   print ('Get a better number')

for i in range(1,4):
    for k in range(3-i,0,-1):
        print(' ' ,end='')
    for j in range(1,i+1):
        print('* ' ,end='')
    print()
    
row=int(input('Give me a number'))
for i in range(1,row+1):
    for k in range(row-i,0,-1):
        print(' ',end=(''))
    for j in range(1,i+1):
        if j==1 or j==i:
            print('$ ',end='')
        else:
            print('  ',end='')
    print()

for i in range(row-1,0,-1):
    for k in range(row-i,0,-1):
        print(' ',end=(''))
    for j in range(1,i+1):
        if j==1 or j==i:
            print('$ ',end='')
        else:
            print('  ',end='')
    print()
"""