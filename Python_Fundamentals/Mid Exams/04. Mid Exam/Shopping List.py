def urgent(add_item):
    products.insert(0, add_item)


def unnecessary(remove_item):
    products.remove(remove_item)


def correct(old_item, new_item):
    for n, i in enumerate(products):
        if i == old_item:
            products[n] = new_item


def rearrange(item_change):
    products.remove(item_change)
    products.append(item_change)

products = input().split("!")
final_products_list = []
command = input()

while command != "Go Shopping!":
    command = command.split()

    if command[0] == "Urgent":
        add_item = command[1]
        if add_item not in products:
            urgent(add_item)

    elif command[0] == "Unnecessary":
        remove_item = command[1]
        if remove_item in products:
            unnecessary(remove_item)

    elif command[0] == "Correct":
        old_item = command[1]
        new_item = command[2]
        if old_item in products:
            correct(old_item, new_item)

    elif command[0] == "Rearrange":
        item_change = command[1]
        if item_change in products:
            rearrange(item_change)

    command = input()

print(*products, sep=", ")
