numbers = [int(x) for x in input().split()]

command = input()
while command != 'END':
    cmd_type, *data = command.split()
    if "Change" in cmd_type:
        paint_number = int(data[0])
        new_number = int(data[1])
        if paint_number in numbers:
            index_paint_num = numbers.index(paint_number)
            numbers.remove(paint_number)
            numbers.insert(index_paint_num, new_number)

    elif 'Hide' in cmd_type:
        paint_number = int(data[0])
        if paint_number in numbers:
            numbers.remove(paint_number)

    elif 'Switch' in cmd_type:
        paint_num_one = int(data[0])
        paint_num_two = int(data[1])
        if paint_num_one in numbers and paint_num_two in numbers:
            index_one = numbers.index(paint_num_one)
            index_two = numbers.index(paint_num_two)
            numbers[index_one], numbers[index_two] = numbers[index_two], numbers[index_one]

    elif 'Insert' in cmd_type:
        index = int(data[0]) + 1
        paint_number = int(data[1])
        if 0 <= index < len(numbers):
            numbers.insert(index, paint_number)

    elif 'Reverse' in cmd_type:
        numbers = numbers[::-1]

    command = input()

print(*numbers)