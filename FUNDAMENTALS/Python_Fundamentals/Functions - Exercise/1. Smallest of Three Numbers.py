num_one = int(input())
num_two = int(input())
num_three = int(input())


def smallest_one(one):
    result = num_one
    return result


def smallest_two(two):
    result = num_two
    return result


def smallest_three(three):
    result = num_three
    return result


if num_one < num_two and num_one < num_three:
    print(smallest_one(num_one))

elif num_two < num_one and num_two < num_three:
    print(smallest_two(num_two))

elif num_three < num_one and num_three < num_two:
    print(smallest_three(num_three))
