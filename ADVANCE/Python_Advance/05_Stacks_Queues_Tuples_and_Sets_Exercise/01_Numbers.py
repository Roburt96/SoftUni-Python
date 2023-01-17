row_one_numbers = set(int(x) for x in input().split())
row_two_numbers = set(int(x) for x in input().split())
n_cmd = int(input())

for i in range(n_cmd):
    cmd_one, cmd_two, *digits = [int(x) if x.isdigit() else x for x in input().split()]
    cmd = cmd_one + cmd_two

    if cmd == 'AddFirst':
        for num in digits:
            row_one_numbers.add(num)

    elif cmd == 'AddSecond':
        for num in digits:
            row_two_numbers.add(num)

    elif cmd == "RemoveFirst":
        for num in digits:
            row_one_numbers.discard(num)

    elif cmd == "RemoveSeconds":
        for num in digits:
            row_two_numbers.discard(num)

    elif cmd == "CheckSubset":
        if row_two_numbers.issubset(row_one_numbers):
            print(True)
        elif not row_two_numbers.issubset(row_one_numbers):
            print(False)


print(*sorted(row_one_numbers), sep=", ")
print(*sorted(row_two_numbers), sep=", ")

