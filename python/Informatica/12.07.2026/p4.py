print(f" {"Topic: Function - Generate (yield)"} ".center(90, '-'))

def numbers():
    yield 1
    yield 2
    yield 3

gen = numbers()

print(next(gen))
print(next(gen))
print(next(gen))
