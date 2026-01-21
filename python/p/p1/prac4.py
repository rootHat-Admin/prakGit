# Example 4: print only odd numbers up to 20

i = 1  # int

while i <= 20:
    if i % 2 == 0:
        i += 1
        continue  # skip even numbers

    print("Odd number:", i)
    i += 1
