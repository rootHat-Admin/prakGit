n = 42
base = 2
result = ""

while n > 0:
    result = str(n % base) + result
    n //= base

print("42 in base 2 =", result)