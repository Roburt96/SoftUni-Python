
def even_odd_filter(**num):
    dict_nums = {}
    for key in num:
        dict_nums[key] = dict_nums.get(key, [])
        if key == 'odd':
            dict_nums[key] = [x for x in num[key] if x % 2 != 0]
        if key == 'even':
            dict_nums[key] = [x for x in num[key] if x % 2 == 0]

    sorted_nums = {}
    for operation, values in sorted(dict_nums.items(), key=lambda item: -len(item[1])):
        sorted_nums[operation] = values
    return sorted_nums


# print(even_odd_filter(
#     odd=[2, 2, 30, 44, 10, 5],
# ))


# print(even_odd_filter(
#     odd=[1, 2, 3, 4, 10, 5],
#     even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
# ))


