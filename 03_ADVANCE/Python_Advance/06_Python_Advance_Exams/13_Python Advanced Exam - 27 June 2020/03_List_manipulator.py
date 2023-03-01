

def list_manipulator(*args):
    list_nums = args[0]
    cmd = args[1]
    poss = args[2]
    nums = [int(x) for x in args[3:]]

    if cmd == 'add' and poss == 'beginning':
        list_nums = nums + list_nums

    elif cmd == 'add' and poss == 'end':
        list_nums += nums

    elif cmd == 'remove' and poss == 'beginning':
        if nums:
            list_nums = list_nums[nums[-1]:]
        else:
            list_nums = list_nums[1:]

    elif cmd == 'remove' and poss == 'end':
        if nums:
            list_nums = list_nums[:-nums[-1]:]
        else:
            list_nums = list_nums[:-1]

    return list_nums

#
# print(list_manipulator([1,2,3], "remove", "end"))
# print(list_manipulator([1,2,3], "remove", "beginning"))
# print(list_manipulator([1,2,3], "add", "beginning", 20))
# print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
# print(list_manipulator([1,2,3], "remove", "beginning", 2))
# print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
# print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))