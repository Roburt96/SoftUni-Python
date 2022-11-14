num_a = int(input())
num_b = int(input())
num_c = int(input())


def sum_num(a, b):
    result = a + b
    return result


def subtract(c):
    result = sum_num(num_a, num_b) - c
    return result


print(subtract(num_c))


