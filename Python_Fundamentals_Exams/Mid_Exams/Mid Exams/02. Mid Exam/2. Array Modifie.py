numbers = list(map(int, input().split(" ")))

command = input()
while command != "end":
    command_type = command.split()
    action = command_type[0]

    if action == "swap":
        swap_one = int(command_type[1])
        swap_two = int(command_type[2])
        numbers[swap_one], numbers[swap_two] = numbers[swap_two], numbers[swap_one]
    elif action == "multiply":
        multi_one = int(command_type[1])
        multi_two = int(command_type[2])
        multiplication = numbers[multi_one] * numbers[multi_two]
        numbers[int(command_type[1])] = multiplication
    elif command == "decrease":
        for pos in range(len(numbers)):
            numbers[pos] -= 1
    command = input()

final_list = [str[i] for i in numbers]

print(', '.join(final_list))



