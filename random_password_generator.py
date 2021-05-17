# Creates a random password of specified length

import random

# User Input
pass_length = int(input("Enter the length of the desired password: "))
characters = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Join together the random selected characters of length pass_length with "" as the sperator
password = "".join(random.sample(characters, pass_length))
print(password)
