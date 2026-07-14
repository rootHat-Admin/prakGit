print(f" {"Topic: Function - *args + **kwargs"} ".center(90, "-"))

def info(*args, **kwargs):
    print("args =", args)
    print("kwargs =", kwargs)

info(
    10,
    20, 
    30,
    name="Ali",
    age=17
)

print("-" * 30)