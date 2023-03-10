numbers = list(map(int, input().split()))

command = input()
while command != 'Finish':
    command_type, *data = command.split()

    if 'Add' in command_type:
        value = int(data[0])
        numbers.append(value)

    elif 'Remove' in command_type:
        value = int(data[0])
        if value in numbers:
            numbers.remove(value)

    elif 'Replace' in command_type:
        value = int(data[0])
        replace_value = int(data[1])
        for i in range(len(numbers)):
            if numbers[i] == value:
                numbers[i] = replace_value
                break

    elif 'Collapse' in command_type:
        value = int(data[0])
        for number in numbers[::-1]:
            if number < value:
                numbers.remove(number)
    command = input()


print(*numbers)

