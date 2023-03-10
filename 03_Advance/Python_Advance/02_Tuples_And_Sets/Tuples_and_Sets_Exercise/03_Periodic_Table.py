number_of_inputs = int(input())
table = set()
for x in range(number_of_inputs):
    compounds = input().split()
    for i in compounds:
        table.add(i)

print(*table, sep="\n")


