print("------------------------------")
print("Use a for loop to print numbers from 10 to 15")

for i in range(10, 16, 1):
    print(i)

print("------------------------------")
print("Use a while loop to print numbers from 5 down to 1.")
i = 5
while i > 0:
    print(i)
    i -= 1

print("------------------------------")
print("Use a for loop to print: Hello 3 times.")

for i in range(3):
    print("Hello")


print("------------------------------")
print("Ask the user for their name until they write Alice.")

name = "Alice"
while name != "Alice":
    name = input("Enter your name: ")
    print("Welcome, Alice!")

print("------------------------------")
