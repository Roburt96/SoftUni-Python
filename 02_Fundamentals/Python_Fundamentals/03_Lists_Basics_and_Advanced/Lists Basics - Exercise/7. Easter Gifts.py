# gift_name = input().split()
# cmd = input()
#
# while cmd != "No Money":
#     cmd_info, *item_info = cmd.split()
#     if "OutOfStock" in cmd_info:
#         for i, name in enumerate(gift_name):
#             if item_info[-1] == name:
#                 gift_name[i] = "None"
#     elif "Required" in cmd_info:
#         lengh = len(gift_name)
#         if lengh > int(item_info[-1]) > 0:
#             gift_name[int(item_info[-1])] = item_info[0]
#     elif "JustInCase" in cmd_info:
#         gift_name[-1] = item_info[-1]
#     cmd = input()
#
# print(" ".join(x for x in gift_name if x != "None"))


def outofstock_(gift_name):
    for i, name in enumerate(gift_names):
        if gift_name == name:
            gift_names[i] = 'None'


def required_(gift_name, index):
    if 0 <= index < len(gift_names):
        gift_names[index] = gift_name


def justincase_(gift_name):
    gift_names[-1] = gift_name



gift_names = input().split()
cmd = input()

while cmd != 'No Money':
    command_type, *data = cmd.split()

    if 'OutOfStock' in command_type:
        name_gift = data[0]
        outofstock_(name_gift)

    elif 'Required' in command_type:
        name_gift = data[0]
        index_gift = int(data[1])
        required_(name_gift, index_gift)

    elif 'JustInCase' in command_type:
        name_gift = data[0]
        justincase_(name_gift)

    cmd = input()

print(" ".join(x for x in gift_names if x != "None"))
