# version = input().split(".")
# num1 = int(version[0])
# num2 = int(version[1])
# num3 = int(version[2])
#
# if num3 + 1 > 9:
#     num2 = num2 + 1
#     num3 = 0
# else:
#     num3 = num3 + 1
#
# if num2 + 1 > 10:
#     num1 = num1 + 1
#     num2 = 0
#
#
# print(f"{num1}.{num2}.{num3}")

version = [int(x) for x in input().split(".")]
new_version = version.copy()
if new_version[-1] + 1 > 9:
    new_version[1] = new_version[1] + 1
    new_version[2] = 0
else:
    new_version[2] = new_version[2] + 1

if new_version[1] + 1 > 10:
    new_version[0] = new_version[0] + 1
    new_version[1] = 0

print(f"{new_version[0]}.{new_version[1]}.{new_version[2]}")

