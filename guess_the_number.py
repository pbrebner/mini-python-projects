# Guess the Number Game

# Computer randomly choses a number and the user has three chances to guess the number

import random

number = random.randint(1, 10)
for i in range(0, 3):
    user_guess = int(input("Guess the Number: "))
    if user_guess == number:
        print("You Win!")
        print("You guess the number right")
    elif user_guess > number:
        print("Your guess is too high")
    elif user_guess < number:
        print("Your guess is too low")
else:
    print("Nice Try, but the number is ", number)
