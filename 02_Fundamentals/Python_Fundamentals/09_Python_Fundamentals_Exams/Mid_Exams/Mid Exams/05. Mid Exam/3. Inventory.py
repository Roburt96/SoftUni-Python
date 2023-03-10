inventory = input().split(", ")
command = input()

while command != "Craft!":

    command = command.split(" - ")
    item = command[-1]

    if "Collect" in command:
        if item not in inventory:
            inventory.append(item)

    if "Drop" in command:
        if item in inventory:
            inventory.remove(item)

    if "Combine Items" in command:
        old_item, new_item = item.split(":")
        if old_item in inventory:
            inventory.insert(inventory.index(old_item) + 1, new_item)

    if "Renew" in command:
        if item in inventory:
            inventory.append(inventory.pop(inventory.index(item)))

    command = input()

print(*inventory, sep=", ")
