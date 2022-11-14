def average_values(input_data):
    attack = 0
    hp = 0
    defence = 0

    for name, stats in input_data.items():
        hp += int(stats['health'])
        defence += int(stats['armor'])
        attack += int(stats['damage'])
    avr_attack = attack / len(input_data)
    avr_hp = hp / len(input_data)
    avr_defence = defence / len(input_data)
    return avr_attack, avr_hp, avr_defence


number_of_dragons = int(input())
dragons_dict = {}
for i in range(number_of_dragons):
    input_command = input()
    color, name, damage, health, armor = input_command.split(' ')
    if 'null' in input_command:
        if 'null' in damage:
            damage = 45
        if 'null' in health:
            health = 250
        if 'null' in armor:
            armor = 10
    if color not in dragons_dict:
        dragons_dict[color] = {}
    if name not in dragons_dict[color]:
        dragons_dict[color][name] = {'damage': damage, 'health': health, 'armor': armor}
    dragons_dict[color][name] = {'damage': damage, 'health': health, 'armor': armor}

for colors, dragons in dragons_dict.items():
    average = average_values(dragons)
    print(f'{colors}::({average[0]:.2f}/{average[1]:.2f}/{average[2]:.2f})')
    for name, stats in sorted(dragons.items()):
        print(f"-{name} -> damage: {stats['damage']}, health: {stats['health']}, armor: {stats['armor']}")
