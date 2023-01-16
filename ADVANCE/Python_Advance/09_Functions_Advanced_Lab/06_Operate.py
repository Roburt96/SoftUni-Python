def operate(*args):
    operator, nums = args[0], args[1:]
    result = 0
    if operator == "+":
        result = sum(x for x in args[1:])
    elif operator == "-":
        f_num = args[1]
        for x in args[2:]:
            f_num -= x
        result = f_num
    elif operator == "*":
        first = 1
        for x in args[1:]:
            first *= x
        result = first
    elif operator == "/":
        first = args[1]
        for x in args[2:]:
            first /= x
        result = first
    return result


