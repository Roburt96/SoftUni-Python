def forward_(step):
    global current_position
    if 0 <= current_position + step < len(houses):
        current_position += step
        houses.pop(step)


def swap_(num_one, num_two):
    first_house = 0
    second_house = 0
    if num_one in houses and num_two in houses:
        first_house = houses.index(num_one)
        second_house = houses.index(num_two)

    houses[first_house], houses[second_house] = houses[second_house], houses[first_house]


def gift_(index, house_num):
    global current_position
    if 0 <= index < len(houses):
        houses.insert(index, house_num)
        current_position = index


def back_(index):
    global current_position
    if 0 <= current_position - index < len(houses):
        current_position -= index
        houses.pop(current_position)


number_of_commands = int(input())
houses = [int(x) for x in input().split()]
current_position = 0


for i in range(number_of_commands):
    command_type, *info = input().split()

    if 'Forward' in command_type:
        steps = int(info[0])
        forward_(steps)
    elif 'Swap' in command_type:
        number1 = int(info[0])
        number2 = int(info[1])
        swap_(number1, number2)
    elif 'Gift' in command_type:
        index = int(info[0])
        house_number = int(info[1])
        gift_(index, house_number)
    elif 'Back' in command_type:
        back_index = int(info[0])
        back_(back_index)

print(f"Position: {current_position}")
print(*houses, sep=', ')

