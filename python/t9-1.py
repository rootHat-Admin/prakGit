# 1 - def
def greet():
    print("Hello World!")

# 2 - def
def greet_name(name):
    print(f"Hello, {name}!")

# 3 - def
def check_name(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

# 4 - def
def  multiplication_table(n):
    for i in range(1 ,10):
        print(f"{n} x {i} = {n*i}")

# 5 - def
def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

# 6 - def
def add(a, b):
    return a + b 

# 7 - def
def max_list(lst):
    maximum = lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
    return maximum

# 8 - def
def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

# 9 - def
def double_list(lst):
    return [x*2 for x in lst]

# 10 - def
def lengths(lst):
    return [len(s) for s in lst]

# 11 - def
def get_keys(d):
    return list(d.keys())

# 12 - def
def get_value(d):
    return list(d.values())

print(get_value({"a":1, "b":2}))

# 13 - def
def find_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
    return None

print(find_key({"a":1, "b":2}, 2))
# 14 - def
def merge_dicts(d1, d2):
    return {**d1, **d2}

print(merge_dicts({"a":1}, {"b":2}))

# 15 - def
def char_count(s):
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    return counts

print(char_count("cyberpunk"))

