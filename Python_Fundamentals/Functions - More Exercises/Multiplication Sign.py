def multiplication(one, two, three):
    if (three > 0 and one < 0 and two < 0) or \
            (two > 0 and one < 0 and three < 0) or \
            (one > 0 and two < 0 and three < 0) or \
            (one > 0 and two > 0 and three > 0):
        return "positive"
    elif one == 0 or two == 0 or three == 0:
        return "zero"
    elif one < 0 or two < 0 or three < 0:
        return "negative"


num_one = int(input())
num_two = int(input())
num_three = int(input())


print(multiplication(num_one, num_two, num_three))
