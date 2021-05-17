# Creates a random password of specified length

import random

pass_length = int(input("Enter the length of the desired password: "))
characters = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
password = "".join(random.sample(characters, pass_length))
print(password)
