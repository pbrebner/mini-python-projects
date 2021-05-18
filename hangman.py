# Simple hangman game

import time
import random

print("Hello, time to play hangman!")
time.sleep(2)
print("Start guessing...\n")
time.sleep(0.5)

# List of secret words
secret_words = ["python", "apple", "tesla", "programming", "creative", "learning"]
word = random.choice(secret_words)
guesses = ""
turns = 5
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end="")
            failed += 1
    if failed == 0:
        print("\nYou won! The word was", word)
        break
    guess = input("\nguess a character: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("\nWrong")
        print("\nYou have ", turns, " more guesses")
        if turns == 0:
            print("\nYou lose")
