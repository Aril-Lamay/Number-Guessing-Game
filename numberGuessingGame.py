from random import random


import random
number = int(random.randrange(1,9))
chance=0
print("|| Number Guessing Game ||")
print("Guess the correct number between 1 and 9")
print("")
while chance < 5:
    guess = int(input("Enter your Guess : "))
    if guess==number:
        print("||| Congratulations!!! You Won |||")
        break
    elif guess != number:
        if guess < number-4:
            print("Your guess was too low")
        elif guess > number+4:
            print("Your guess was too high")
        elif guess < number:
            print("Your guess is a little low, try a bit higher")
        elif guess > number:
            print("You guess is little high, try something lower")
    chance = chance + 1
if not chance < 5:
    print("")
    print("You LOSE, the number is ", number)