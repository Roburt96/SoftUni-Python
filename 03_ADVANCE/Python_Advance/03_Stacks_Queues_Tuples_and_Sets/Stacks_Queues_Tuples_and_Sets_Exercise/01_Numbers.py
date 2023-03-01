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


# first = set(int(x) for x in input().split())
# second = set(int(x) for x in input().split())
#
# func = {
#     "Add First": lambda x: [first.add(el) for el in x],
#     "Add Second": lambda x: [second.add(el) for el in x],
#     "Remove First": lambda x: [first.discard(el) for el in x],
#     "Remove Second": lambda x: [second.add(el) for el in x],
#     "Check Subset": lambda : print(True) if first.issubset(second) or second.issubset(first) else print(False)
# }
#
# for _ in range(int(input())):
#     first_command, *data = input().split()
#     command = first_command + " " + data.pop(0)
#
#     if data:
#         func[command]([int(x) for x in data])
#     else:
#         func[command]()
#
# print(*sorted(first), sep=", ")
# print(*sorted(second), sep=", ")
