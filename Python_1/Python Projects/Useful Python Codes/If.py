from lib2to3.pgen2.literals import evalString
import random
from re import U 
"""
a=eval(input('Give me a your marks'))

if (a>=75 and a<=100):
    print('You got an A')
elif (a>=60 and a<=74):
    print('You got a B')
elif (a>=45 and a<=59):
    print('You got a C')

else:
    print('You got a D')
   
comp=random.randint(1,10) 
  
l=eval(input('give me your number guess'))
if (l==comp):
    print('You guessed {} which is a lucky number!'.format(l))
else:
    print('Sorry you guessed wrong.')
    print('lucky numner:',comp)
    
          
#guess the number 

comp=random.randint(1,100) 
  
l=eval(input('give me your number guess'))
if (l==comp):
    print('You guessed {} which is a the correct number'.format(l))
else:
    print('Sorry your guess was wrong. ')
 
    


        #rock paper scissor 
l=['rock','scissor','paper']
u=0
c=0
for i in range(1,4):
    comp=random.choice(l)
    user=input('Chose rock, paper, or scissors')

    if (user=='rock') or (user=='scissor') or (user== 'paper'):
        print('Good job let us see whether your choice of {} will win the computer!'.format(user))
        if((comp=='rock' and user== 'scissor') or  (comp=='scissor'and user == 'paper') or (comp== 'paper' and user=='rock')):
            print('You Lost')
            c=c+1
        elif(comp==user):
            print('You tied')

        else:
            print('Your choice of {} won against {}'.format(user,comp))
            u=u+1
    
    else:
        print('Your guess is invalid make sure you type Rock,Paper or Scissors,  ')
print(' Your win score {}  and the computer score is {}'.format(u,c))

if c>u:
    print('The computer won')
elif c==u:
    print('You and the computer tied')
else:
    print('You won')
 """""

###write a python program to get a number from user and print the multiplication table of tht
u=int(input('Give me a number'))
for i in range (1,13):
    z=u*i
    print('{}x{}={}'.format(u,i,z) )


    
