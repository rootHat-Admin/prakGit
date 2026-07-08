# 3. Scopes of visibility: global and nonlocal

# 3 - nonlocal

def outer():
    msg = "Hello"
    def inner():
        nonlocal msg
        msg = "Bay!"
    inner()
    print(msg)
outer()