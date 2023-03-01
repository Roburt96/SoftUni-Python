numbers = [int(x) for x in input().split(", ")]
max_number = max(numbers)

boundary = 0

while True:
    grp_list = []
    boundary += 10

    for check_num in numbers:
        if check_num <= boundary:
            grp_list.append(check_num)
    print(f"Group of {boundary}'s: {grp_list}")
    [[numbers.remove(num_numbers) for num_numbers in numbers if num_numbers == num_grp_list]
     for num_grp_list in grp_list]


    if len(numbers) == 0:
        break

