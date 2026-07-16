print(f" {"Topic: Function - Recursion "} ".center(90, '-'))

def count(n):
    print(n)
    count(n - 1)

print(count(5))