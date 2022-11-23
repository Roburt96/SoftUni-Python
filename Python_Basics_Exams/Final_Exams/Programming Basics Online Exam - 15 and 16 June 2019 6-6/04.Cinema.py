capacity = int(input())
price = 0
seats_take = 0

command = input()
while command != "Movie time!":
    seats = int(command)
    seats_take += seats

    if capacity < seats_take:
        break
    price += seats * 5
    if seats % 3 == 0:
        price -= 5

    command = input()

if command == "Movie time!":
    print(f"There are {capacity - seats_take} seats left in the cinema.")
else:
    print(f"The cinema is full.")
print(f"Cinema income - {price} lv.")
