B = False
numbers = [int(x) for x in input().split(" ")]
average_number = sum(numbers) / len(numbers)
numbers.sort(reverse=True)
print_num = B

for index, num in enumerate(numbers):
    if index <= 4 and num > average_number:
        print(num, end=" ")
        print_num = True
    if not print_num:
        print("No")
        break
















