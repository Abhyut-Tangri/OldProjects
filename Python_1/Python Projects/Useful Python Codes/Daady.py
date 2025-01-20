import random
kid = input(print('Kids Name = '))
DADS = ('Barry','Gary','Max','Becker','Drew', 'Ali', 'Carson', 'Harrison')
name = random.choice(DADS)
print('Your name is {} and your dad is {}'.format(kid,name))