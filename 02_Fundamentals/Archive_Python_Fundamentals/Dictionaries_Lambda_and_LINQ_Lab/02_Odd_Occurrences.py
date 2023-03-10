strings = [x for x in input().lower().split()]
count_strings = {}
list_strings = []
for i in strings:
    if i not in count_strings:
        count_strings[i] = 1
    else:
        count_strings[i] += 1

for z in count_strings:
    if count_strings[z] % 2 != 0:
        list_strings.append(z)

print(*list_strings, sep=", ")
# for key in count_strings:
#     print(f"{count_strings[key]}", sep=", ")
