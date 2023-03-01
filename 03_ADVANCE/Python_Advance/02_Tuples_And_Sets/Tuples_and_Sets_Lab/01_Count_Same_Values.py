numbers = tuple(map(float, input().split()))
num_counter = {}

for num in range(len(numbers)):
    x = numbers.count(numbers[num])
    if numbers[num] not in num_counter:
        num_counter[numbers[num]] = x

for key, value in num_counter.items():
    print(f'{key} - {value} times')

