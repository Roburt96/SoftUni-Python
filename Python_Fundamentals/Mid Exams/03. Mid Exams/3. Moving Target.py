targets = [int(n) for n in input().split()]
command = input()


def shoot(index, power):
    if 0 <= index < len(targets):
        targets[index] -= power
        if targets[index] <= 0:
            del targets[index]


def add(index, value):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        print("Invalid placement!")


def strike(index, radius):
    radius_to_zero = index - radius
    radius_to_len = index + radius
    if radius_to_zero >= 0 and radius_to_len < len(targets):
        del targets[radius_to_zero:radius_to_len + 1]
    else:
        print(f"Strike missed!")


while command != "End":
    info = command.split()

    if info[0] == "Shoot":
        shoot(int(info[1]), int(info[2]))
    elif info[0] == "Add":
        add(int(info[1]), int(info[2]))
    elif info[0] == "Strike":
        strike(int(info[1]), int(info[2]))
    command = input()

print(*targets, sep="|")


