def update_dict_(name, point):
    plant_dict[name] = plant_dict.get(name, {'rarity': 0, 'rating': []})
    plant_dict[name]['rarity'] = int(point)


def rate_(plant, rating):
    if plant in plant_dict:
        plant_dict[plant]['rating'].append(rating)
    else:
        print('error')


def update_(update_plant, new_rarity):
    if update_plant in plant_dict:
        plant_dict[update_plant]['rarity'] = new_rarity
    else:
        print('error')


def reset_(reset_plant):
    if reset_plant in plant_dict:
        plant_dict[reset_plant]['rating'] = []
    else:
        print('error')


number_of_lines = int(input())
plant_dict = {}

for i in range(number_of_lines):
    name_plant, info = input().split("<->")
    name = name_plant
    rarity = int(info)
    update_dict_(name, rarity)

commands = input()
while commands != 'Exhibition':
        cmd_type, info = commands.split(": ")

        if 'Rate' in cmd_type:
            info = info.split(" - ")
            rate_plant = info[0]
            rating = int(info[1])
            rate_(rate_plant, rating)

        elif 'Update' in cmd_type:
            info = info.split(" - ")
            update_plant = info[0]
            new_rating = int(info[1])
            update_(update_plant, new_rating)

        elif 'Reset' in cmd_type:
            reset_plant = info
            reset_(reset_plant)

        commands = input()

print("Plants for the exhibition:")
for key in plant_dict.keys():
    average_rating = 0
    if plant_dict[key]['rating']:
        average_rating = sum(plant_dict[key]['rating']) / len(plant_dict[key]['rating'])
    print(f"- {key}; Rarity: {plant_dict[key]['rarity']}; Rating: {average_rating:.2f}")



