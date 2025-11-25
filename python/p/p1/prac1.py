# Example 1: calculate final price with discount

price_str = input("Enter product price: ")  # str
price = float(price_str)  # str > float

discount = 10  # int
has_discount = True  # bool

if has_discount:
    final_price = price - price * discount / 100
else:
    final_price = price

print("Final price:", final_price)
