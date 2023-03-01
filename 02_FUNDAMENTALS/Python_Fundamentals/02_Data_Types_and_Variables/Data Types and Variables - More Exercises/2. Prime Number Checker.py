num = int(input())
flag = False

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            flag = True
            break
if flag:
    print(False)
else:
    print(True)


# def prime_Check(number):
#     global Flag
#     if number > 1:
#         for i in range(2, number):
#             if number % i == 0:
#                 flag = True
#                 break
#
#
# num = int(input())
# flag = False
#
# if flag:
#     print(False)
# else:
#     print(True)
