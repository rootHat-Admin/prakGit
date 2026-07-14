print(f" {"Topic: Function - DECORATOR"} ".center(90, '-'))

def decorator(func):
    def wrapper():
        print("Before executing the function")
        func()
        print("After executing the function")
    return wrapper

@decorator
def hello():
    print("Hello!")

hello()