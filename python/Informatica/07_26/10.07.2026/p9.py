print(f" {"Topic: Function - nonlocal"} ".center(90, "-"))

def outer():
    money = 100
    def inner():
        nonlocal money
        money += 50
    inner()

    print(money)

outer()