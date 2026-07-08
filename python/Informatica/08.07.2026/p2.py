# 2. Arguments: *args and kwargs

def example(*args, **kwargs):
    print(f"Positional: {args}")
    print(f"Named: {kwargs}")

example(1, 2, 3, user="Alex", status="admin")
# print: (1, 2, 3) and {'user': 'Alex', 'status': 'admin'}