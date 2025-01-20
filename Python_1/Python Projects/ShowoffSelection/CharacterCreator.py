print('You have 30 points to spend on Strength, Health, Wisdom, and Dexterity ')
totalpoints = 30
dexterity = int(input('Would you like to spend points on dexterity?'))

if dexterity == "yes":
    dexteritypts = int(input('How many points would you like to spend on dexterity?'))
    print ('You have' , totalpoints - dexteritypts,'left over')
    areusuredex =int(input('Are you sure you would like to spend one dexterity?'))
     if areusuredex == 'No':
        areusuredex2 = int(input('How much would you like to spend'))
        print(totalpoints - areusuredex2)

health = int(input('Would you like to spend points on health?'))
if health == "yes":
    healthpts = int(input('How many points would you like to spend on health?'))
    print (totalpoints - dexteritypts - healthpts)
    areusurehp =int(input('Are you sure you would like to spend on health?'))
     if areusurehp == 'No':
        areusurehp2 = int(input('How much would you like to spend'))
        print(totalpoints - dexteritypts - areusurehp2)

