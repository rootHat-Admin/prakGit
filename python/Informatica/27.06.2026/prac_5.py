# Practice for Topic: Conditional Statements (if, elif, else).

dogAge = int(input("Enter youe dog age: "))

if dogAge == 0:
    print("Bro dog 0 age")
elif dogAge <=2:
    print(f"The age of your dog in terms of human years: {dogAge * 5.25}")
else:
    print(f"The age of your dog in terms of human years: {(dogAge - 2 )* 4 + 10.5}")