print(f" {"Topic: Function - NOD "} ".center(90, '-'))

def gcd(a, b):
    if b==0:
        return a
    
    return gcd(b,a%b)

print(gcd(44,218))