# random module - is designed to get some ramdom values 
# sometimes we need to find the square and square root of a number we use math module

import random
print(random.randint(1,20))
print(random.choice("computer science"))
print(random.random()) # the empty bracets gives you number between 0 and 1


import random
number = random.randint(1,10)
print("I have guessed a number, plz try and tell me what is the number: ")

while True:
    guess = int(input("Enter your guessed number: "))
    if guess == number:
        print("Welldone")
        break
    else:
        print("try again")