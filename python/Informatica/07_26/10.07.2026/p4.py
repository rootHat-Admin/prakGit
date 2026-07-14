print(f" {"Topic: Function - **kwargs"} ".center(90, "-"))

def person(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, "->", value)
    
person(
    name="Ali",
    age=17,
    city="Almaty"
)
