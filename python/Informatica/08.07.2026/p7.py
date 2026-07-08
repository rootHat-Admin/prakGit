# 4. Lambda function

# 2 - Lambda with filter()

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens) # [2, 4, 6]