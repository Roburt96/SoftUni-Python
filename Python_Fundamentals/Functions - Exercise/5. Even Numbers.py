numbers = list(map(int, input().split(" ")))


def even(num):
    result = list(filter(lambda x: x % 2 == 0, numbers))
    return result


print(even(numbers))
