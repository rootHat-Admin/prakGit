print(f" {"Topic: Function - Recursive "} ".center(90, '-'))

def f(n):
    if n == 0:
        return
    
    print(n)
    f(n-1)
    print(n)

f(5)