first_num = int(input())
second_num = int(input())

for number in range(first_num, second_num + 1):
    number_to_str = str(number)
    odd_sum = 0
    even_sum = 0

    for index, digit in enumerate(number_to_str):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    if odd_sum == even_sum:
        print(number, end=" ")
