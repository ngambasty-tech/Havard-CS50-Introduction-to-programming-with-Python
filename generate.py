import random #the whole random library

from random import choice

# coin = random.choice(["head","tail"])
coin = choice(["head","tail"])
# print(coin)

number = random.randint(1, 20)
print(number)

names = ["Alice", "Bob", "Charlie", "David"]
random.shuffle(names)
for name in names:
    print(name)