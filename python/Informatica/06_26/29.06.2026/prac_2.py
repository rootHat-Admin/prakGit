# topic: Loop - while\for

total_sum = 0
user_number = int(input("Enter a number to add (enter 0 to finish): "))

while user_number != 0:
    total_sum += user_number
    user_number = int(input("Enter another number (ot 0 to stop): "))

print(f"The final sum is: {total_sum}")