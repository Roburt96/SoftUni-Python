number_of_inputs = int(input())
row = 0
total = 0
odd_num = set()
even_num = set()

for i in range(number_of_inputs):
    name = input()
    row += 1
    for ch in name:
        ord_ch = ord(ch)
        total += ord_ch
    divide_total = total // row
    if divide_total % 2 == 0:
        odd_num.add(divide_total)
    else:
        even_num.add(divide_total)
    total = 0

odd_num.symmetric_difference_update(even_num)
print(*odd_num, sep=", ")
