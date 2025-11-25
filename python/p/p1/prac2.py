# Example 2: check what type of number it is

number_str = input("Enter a number: ")
number = int(number_str)  # str > int

if number > 0:
    result = "positive"  # str
elif number < 0:
    result = "negative"
else:
    result = "zero"

is_even = number % 2 == 0  # bool

print("Number", number, "is", result)
if is_even:
    print("It is even.")
else:
    print("It is odd.")
