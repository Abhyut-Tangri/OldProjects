while(True):
    age=int(input('What is your age'))
    if (age >=0):
        break
    else:
        print('your age of {} is not valid'.format(age))
print(age)