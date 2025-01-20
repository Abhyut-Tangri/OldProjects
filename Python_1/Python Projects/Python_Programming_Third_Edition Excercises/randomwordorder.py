import random
WORDS = ("OVERUSED", "CLAM", "GUAM", "TAFFETA", "PYTHON")
word = random.choice(WORDS)
words = word * 5
print(words)
while word in word:
    continue