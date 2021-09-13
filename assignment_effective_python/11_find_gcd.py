import math


def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def return_gcd(a, b):
    return math.gcd(a, b)


print(find_gcd(90, 24))
print(return_gcd(90, 24))