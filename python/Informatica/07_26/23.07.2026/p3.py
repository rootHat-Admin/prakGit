print(f" {"Topic: Function - NODE through recursion — Euclid's algorithm "} ".center(90, '-'))

def gcd(a, b):
    if b == 0:
        return a
    
    return gcd(b, a % b)

print(gcd(48, 18))