print(f" {"Topic: Function - The sum of the digits through recursion "} ".center(90, '-'))


def sum_digits(n):
    if n == 0:
        return 0 
    return n % 10 + sum_digits(n // 10)

print(sum_digits(12345))