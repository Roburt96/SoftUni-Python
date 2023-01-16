
strings = [x for x in input().split()[::-1]]
new_strings = []
for ch in strings:
    if len(ch) != 2:
        strings.remove(ch)

for i in strings:
    for num in range(len(i) - 1):
        second_num = i[num]
        first_num = i[-1]
        new_num = first_num + second_num
        new_strings.append(new_num)

s = ''.join(new_strings)
print(s)
print(bytes.fromhex(s).decode('utf-8'))



# x = ''.join(strings)
# s = str(x)
# print(bytes.fromhex(s).decode('utf-8'))

