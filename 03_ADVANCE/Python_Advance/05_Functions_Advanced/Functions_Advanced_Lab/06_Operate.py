from functools import reduce
# def operate(*args):
#     operator = args[0]
#     result = 0
#     if operator == "+":
#         result = sum(x for x in args[1:])
#     elif operator == "-":
#         f_num = args[1]
#         for x in args[2:]:
#             f_num -= x
#         result = f_num
#     elif operator == "*":
#         first = 1
#         for x in args[1:]:
#             first *= x
#         result = first
#     elif operator == "/":
#         first = args[1]
#         for x in args[2:]:
#             first /= x
#         result = first
#     return result

def operate(*args):
    operator = args[0]
    nums = args[1:]
    if operator == "*":
        return reduce(lambda x, y: x*y, nums)
    elif operator == '-':
        return reduce(lambda x, y: x-y, nums)
    elif operator == '+':
        return reduce(lambda x, y: x+y, nums)
    elif operator == '/':
        return reduce(lambda x, y: x/y, nums)



print(operate("-", 8, 2))