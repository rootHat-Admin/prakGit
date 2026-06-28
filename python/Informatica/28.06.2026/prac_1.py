amount = int(input("Enter your amount: "))

if amount < 0:
    print("Incorrect amount")
elif 0 <= amount <= 999:
    print(f"The your amount '{amount}$', there is no discount (0%)")
elif 1000 <= amount <= 4999:
    sym = amount * 0.05
    total = amount - sym 
    print("Congratulations on getting a 5% discount.")
    print(f"Total amount to be paid {totalm}")
else:
    sym = amount * 0.10
    total = amount - sym 
    print("Congratulations on getting a 10% discount.")
    print(f"Total amount to be paid {total}")