from itertools import permutations


def possible_permutations(nums):
    for i in list(permutations(nums)):
        yield list(i)





[print(n) for n in possible_permutations([1, 2, 3])]