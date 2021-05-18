# Guess the Number Game

# Computer randomly choses a number and the user has three chances to guess the number

import random

number = random.randint(1, 10)
for i in range(0, 3):
    user_guess = int(input("Guess the Number [1-10]: "))
    if user_guess == number:
        print("You Win!")
        print("You guessed the correct number")
        break
    elif user_guess > number:
        print("Your guess is too high")
    elif user_guess < number:
        print("Your guess is too low")
else:
    print("Nice Try, but the number is ", number)
