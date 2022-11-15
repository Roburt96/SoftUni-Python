# def update_dict_(name, point):
#     plant_dict[name] = plant_dict.get(name, {'rarity': 0, 'rating': []})
#     plant_dict[name]['rarity'] = int(point)
#
#
# def rate_(plant, rating):
#     if plant in plant_dict:
#         plant_dict[plant]['rating'].append(rating)
#     else:
#         print('error')
#
#
# def update_(update_plant, new_rarity):
#     if update_plant in plant_dict:
#         plant_dict[update_plant]['rarity'] = new_rarity
#     else:
#         print('error')
#
#
# def reset_(reset_plant):
#     if reset_plant in plant_dict:
#         plant_dict[reset_plant]['rating'] = []
#     else:
#         print('error')
#
#
# number_of_lines = int(input())
# plant_dict = {}
#
# for i in range(number_of_lines):
#     name_plant, info = input().split("<->")
#     name = name_plant
#     rarity = int(info)
#     update_dict_(name, rarity)
#
# commands = input()
# while commands != 'Exhibition':
#         cmd_type, info = commands.split(": ")
#
#         if 'Rate' in cmd_type:
#             info = info.split(" - ")
#             rate_plant = info[0]
#             rating = int(info[1])
#             rate_(rate_plant, rating)
#
#         elif 'Update' in cmd_type:
#             info = info.split(" - ")
#             update_plant = info[0]
#             new_rating = int(info[1])
#             update_(update_plant, new_rating)
#
#         elif 'Reset' in cmd_type:
#             reset_plant = info
#             reset_(reset_plant)
#
#         commands = input()
#
# print("Plants for the exhibition:")
# for key in plant_dict.keys():
#     average_rating = 0
#     if plant_dict[key]['rating']:
#         average_rating = sum(plant_dict[key]['rating']) / len(plant_dict[key]['rating'])
#     print(f"- {key}; Rarity: {plant_dict[key]['rarity']}; Rating: {average_rating:.2f}")




class Plant:

    def __init__(self, plant_name):
        self.plant_name = plant_name
        self.rarity = 0
        self.rating = []

    def add_rarity_(self, rarity):
        self.rarity += rarity

    def rate_(self, rating):
        self.rating.append(rating)

    def update_(self, new_rarity):
        self.rarity = new_rarity

    def reset_(self):
        self.rating = []

    def __repr__(self):
        if len(self.rating) > 0:
            return f"- {self.plant_name}; Rarity: {self.rarity}; Rating: {sum(self.rating) / len(self.rating):.2f}"
        else:
            return f"- {self.plant_name}; Rarity: {self.rarity}; Rating: {sum(self.rating):.2f}"

number_of_plants = int(input())
plant_information = {}
for i in range(number_of_plants):
    name, rarity = [int(x) if x.isdigit() else x for x in input().split("<->")]
    plant_information[name] = plant_information.get(name, Plant(name))
    plant_information[name].add_rarity_(rarity)

command = input()
while command != 'Exhibition':
    cmd_type, info = command.split(": ")

    if cmd_type == 'Rate':
        info = info.split(" - ")
        plant_name = info[0]
        plant_rating = int(info[1])
        if plant_name not in plant_information:
            print('error')
        else:
            plant_information[plant_name].rate_(plant_rating)

    elif cmd_type == 'Update':
        info = info.split(" - ")
        plant_name = info[0]
        new_rarity = int(info[1])
        if plant_name not in plant_information:
            print('error')
        else:
            plant_information[plant_name].update_(new_rarity)

    elif cmd_type == 'Reset':
        plant_name = info
        if plant_name not in plant_information:
            print('error')
        else:
            plant_information[plant_name].reset_()

    command = input()

if plant_information:
    print("Plants for the exhibition:")
    for plants in plant_information.values():
        print(plants)
