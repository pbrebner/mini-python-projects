# Simulates the roll of a 6 sided die
import random

while int(input("Press 1 to roll the die or 0 to exit:\n")):
    print("Die Roll: ", random.randint(1, 6))
