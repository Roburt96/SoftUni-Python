def loot(items):
    for i in range(1, len(items)):
        if command[i] not in treasure_chest:
            treasure_chest.insert(0, items[i])


def drop(drop_item):
    treasure_chest.append(treasure_chest.pop(drop_item))


def steal(steal_items):
    steal_treasure = treasure_chest[len(treasure_chest) - steal_items:len(treasure_chest) + 1]
    print(*steal_treasure, sep=', ')
    del treasure_chest[len(treasure_chest) - steal_items:len(treasure_chest) + 1]


treasure_chest = input().split("|")

command = input()

while command != 'Yohoho!':
    command = command.split()

    if command[0] == "Loot":
        loot(command)
    elif command[0] == "Drop":
        drop_item = int(command[1])
        if 0 <= drop_item < len(treasure_chest):
            drop(drop_item)

    elif command[0] == "Steal":
        steal_item = int(command[1])
        if steal_item >= len(treasure_chest):
            print(*treasure_chest, sep=", ")
            treasure_chest.clear()
            break
        else:
            steal(steal_item)

    command = input()

total_sum = sum([len(element) for element in treasure_chest])


if len(treasure_chest) > 0:
    print(f"Average treasure gain: {total_sum / len(treasure_chest):.2f} pirate credits.")
else:
    print("Failed treasure hunt.")

