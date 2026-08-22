print(f" {"22.08.2026"} ".center(90, '='))
print(f" {"Python_Practice_Exam | Topic: Basics | Exercise 4"} ".center(90, '-'))

ageUser = int(input("Enter your age please: "))
coupon_input = input("Do you have a coupon? (yes/no): ")
has_coupon = (coupon_input == "yes")

get_discount = (ageUser >= 65) or has_coupon

print("Eligtible for discount:", get_discount)