numbers = list(map(int, input().strip().split(" ")))
numbers_to_remove = int(input())

for n in range(numbers_to_remove):
    numbers.remove(min(numbers))

print(*numbers, sep=", ")
