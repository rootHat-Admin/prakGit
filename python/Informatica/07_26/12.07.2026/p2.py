print(f" {"Topic: Function - Closures"} ".center(90, '-'))

def outer():
    x = 10

    def inner():
        print(x)

    return inner

func = outer()
func()