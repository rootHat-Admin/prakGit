def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# print(is_prime(7)) # True
# print(is_prime(10)) # False

def string_length(s):
    return len(s)

# print(string_length("Hello"))  # 5

import random

def random_smile():
    smiles = ["😀", "😂", "😎", "🤔", "😴", "🥳"]
    return random.choice(smiles)

print("Your smiley:", random_smile())
