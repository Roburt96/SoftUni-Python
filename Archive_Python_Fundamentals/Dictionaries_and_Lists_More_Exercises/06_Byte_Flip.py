
# strings = [x for x in input().split()]
#
# for ch in strings:
#     if len(ch) != 2:
#         strings.remove(ch)
# print(strings)
# strings.reverse()
# print(strings)
#
# new_list = []
# for i in range(len(strings)):
#     x = hex(int(strings[i]))
#     new_list.append(x)
# print(new_list)


# num = ['21', '23', '44', '55', '22', '6F']
# s = [','.join('{0:.2f}'.format(x) for x in num)]
# print(s)

# new_strings = []
#
# for i in strings:
#     for num in range(len(i) - 1):
#         second_num = i[num]
#         first_num = i[-1]
#         new_num = first_num + second_num
#         new_strings.append(new_num)

# num = '6F'
# h1 = hex(num)
# print("The ", num, " in hexadecimal is: ", h1[2:])
