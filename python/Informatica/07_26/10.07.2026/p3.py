print(f" {"Topic: Function - *args"} ".center(90, "-"))

def total(*args):
    print("Tuple", args)
    s = 0
    for number in args:
        s += number

    return s

print(total(1, 2, 3))
print(total(5, 10))
print(total(100))

