numbers = [int(number) for number in input().split(", ")]
list_without_zeros = []
list_with_zeros = []
for i in numbers:
    if i == 0:
        list_with_zeros.append(i)
    elif i != 0:
        list_without_zeros.append(i)

final_list = list_without_zeros + list_with_zeros

print(final_list)
