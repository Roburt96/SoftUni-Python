# number_of_usernames = int(input())
# usernames = set()
#
# for i in range(number_of_usernames):
#     names = input()
#     usernames.add(names)
#
# print("\n".join(usernames))

number_of_usernames = int(input())
usernames = set([input() for x in range(number_of_usernames)])
print("\n".join(usernames))