from collections import deque
quantity_of_water = int(input())
queue = deque()
name = input()
while name != 'Start':
    queue.append(name)
    name = input()

command = input()
while command != 'End':
    if 'refill' in command:
        litter_to_add = command.split(" ")
        litters = int(litter_to_add[1])
        quantity_of_water += litters

    else:
        liters = int(command)
        if liters <= quantity_of_water:
            quantity_of_water -= liters
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")
    command = input()

print(f"{quantity_of_water} liters left")


