n = int(input())
numbers = []
filtered = []

for i in range(n):
    num = int(input())
    numbers.append(num)

command = input()

if command == "even":
    for number in numbers:
        if number % 2 == 0:
            filtered.append(number)
elif command == "odd":
    for number in numbers:
        if number % 2 != 0:
            filtered.append(number)
elif command == "negative":
    for number in numbers:
        if number < 0:
            filtered.append(number)
elif command == "positive":
    for number in numbers:
        if number > 0:
            filtered.append(number)

print(filtered)
