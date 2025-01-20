import random
triviachoice = ['Sports']
trivia = random.choice(triviachoice)
print('welcome to trivia game...')

if trivia == 'Sports':
    trivia1 = int(input('what was the first point scored in the 2017-2018 finals?'))
    if trivia1 == 'Goaltending':
        print('Yes you got it right!')
        if trivia1 != 'Goal tending':
            print('You got it wrong!')
            trivia2 = int(input('What is Tom Bradys jersy NO.?'))
            if trivia2 == 12 :
                print('You got it right!') 
                if trivia2 != 12:
                    print('you got it wrong.')