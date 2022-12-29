row_one_numbers = set(int(x) for x in input().split())
row_two_numbers = set(int(x) for x in input().split())
n_cmd = int(input())

for i in range(n_cmd):
    cmd_one, cmd_two, *digits = [int(x) if x.isdigit() else x for x in input().split()]
    cmd = cmd_one + cmd_two
    if cmd == 'AddFirst':
        [row_one_numbers.add(digit) for digit in digits[1::]]
    elif cmd == 'AddSecond':
        [row_two_numbers.add(digit) for digit in digits[1::]]
    elif cmd == "RemoveFirst":
        [row_one_numbers.discard(i) for i in digits[1::]]
    elif cmd == "RemoveSeconds":
        [row_two_numbers.discard(i) for i in digits[1::]]
    elif cmd == "CheckSubset":
        if row_two_numbers.issubset(row_one_numbers):
            print(True)
        elif not row_two_numbers.issubset(row_one_numbers):
            print(False)

sorted_first_row = sorted(row_one_numbers)
sorted_second_row = sorted(row_two_numbers)
print(*sorted_first_row, sep=", ")
print(*sorted_second_row, sep=", ")


