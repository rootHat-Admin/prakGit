# Example 3: sum numbers form 1 to N

n_str = input("Enter integer N: ")
n = int(n_str)

total = 0 # int

for i in range(1, n + 1):
    total += i

    # stop if total > 100
    if total > 100:
        print("Sum is greater that 100 at number", i)
        break # stop loop

print("Current sum:", total)