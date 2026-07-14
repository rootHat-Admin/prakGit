print(f" {"Topic: Function - Closures-2"} ".center(90, '-'))

def multiplier(n):
    def  multiply(x):
        return x * n

    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(5))
print(triple(5))