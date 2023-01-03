def numbers_searching(*args):
    numbers = {}
    missing_number = []
    min_num = min(args)
    max_num = max(args)
    num = min_num
    for i in args:
        if num not in args:
            missing_number.append(num)
            break
        num += 1

    for key in args:
        numbers[key] = numbers.get(key, 0) + 1

    result = []

    for key, value in sorted(numbers.items(), key=lambda x: x[0]):
        if value > 1:
            result.append(key)

    missing_number.append(result)
    return missing_number





print(numbers_searching(1, 2, 4, 2, 5, 4))
print()
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print()
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))