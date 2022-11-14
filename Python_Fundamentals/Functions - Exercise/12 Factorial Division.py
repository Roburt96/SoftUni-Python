import math

number_one = int(input())
number_two = int(input())


def factorial(a, b):
    one = math.factorial(a)
    two = math.factorial(b)
    return f"{(one / two):.2f}"


print(factorial(number_one, number_two))
