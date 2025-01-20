import random
kid = input(print('Kids Name = '))
choice = int(input('Would you like a grandpa or dad name?'))
DADS = ('Barry''Gary''Max''Becker''Drew' 'Ali' 'Carson' 'Harrison')
namedad = random.choice(DADS)
if choice == 'Dad':
    print('Your dad name is ' , namedad)

GRAMPS = ('Harry''Larry''Jax''Decker''Trew' 'Hali' 'Larson' 'Barrison')
gawps = random.choice(GRAMPS)

if choice == 'gramps':
    print(gawps)

print('Thank You for using Daady.py')


