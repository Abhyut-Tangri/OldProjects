import random
import string

def RandomPasswords (stringLength=10):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

print("Generating Three Random Passwords ")
print ('First Password Choice ', RandomPasswords() )
print ('Second Password Choice', RandomPasswords(10) )
print ('Third Password Choice',  RandomPasswords(10) )
print ('Copy and paste one of these three passwords to have a foolproof password!' )


