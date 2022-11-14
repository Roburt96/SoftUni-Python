numbers = [float(n) for n in input().split()]


def round_num(num):
    result = [round(num) for num in numbers]
    return result


print(round_num(numbers))




