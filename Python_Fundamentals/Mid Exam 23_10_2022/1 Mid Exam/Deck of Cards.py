def add_(add_card):
    if add_card not in card_list:
        card_list.append(add_card)
        print("Card successfully added")
    else:
        print("Card is already in the deck")


def remove_(remove_card):
    if remove_card in card_list:
        card_list.remove(remove_card)
        print(f"Card successfully removed")
    else:
        print("Card not found")


def removeAt_(index_to_remove):
    if 0 <= index_to_remove < len(card_list):
        card_list.pop(index_to_remove)
        print(f"Card successfully removed")
    else:
        print("Index out of range")


def insert_(index_to_insert, card_to_add):
    if 0 <= index_to_insert < len(card_list):
        if card_to_add not in card_list:
            card_list.insert(index_to_insert, card_to_add)
            print(f"Card successfully added")
        else:
            print(f"Card is already added")
    else:
        print(f"Index out of range")


card_list = input().split(', ')
commands_count = int(input())

for i in range(commands_count):
    command = input().split(", ")

    if 'Add' in command:
        card_add = command[1]
        add_(card_add)
    elif 'Remove' in command:
        card_remove = command[1]
        remove_(card_remove)
    elif 'Remove At' in command:
        index = int(command[1])
        removeAt_(index)
    elif 'Insert' in command:
        index_insert = int(command[1])
        card_to_add = command[2]
        insert_(index_insert, card_to_add)

print(', '.join(card_list))
