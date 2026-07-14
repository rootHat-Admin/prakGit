# Topic: Python (Dictionaries)

d = {"name": "goto", "age": 1923, "type": "Car"}

# 1) .get()
print("=== .get() ===")
res = d.get("agee", "Error!!!")
print(res)

# 2) .keys()
print("=== .keys() ===")
all_keys = d.keys()
print(list(all_keys))

# 3) .values()
print("=== .values() ===")
all_values = d.values()
print(list(all_values))

# 4) .items()
print("=== .items() ===")
for key, value in d.items():
    print(f"Key: {key}, Value: {value}")
