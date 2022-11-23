player_name = input()
starting_points = 301
goodshots = 0
badshots = 0

while starting_points != 0:
    shot = input()
    if shot == "Retire":
        print(f"{player_name} retired after {badshots} unsuccessful shots.")
        break

    points = int(input())
    if shot == "Single":
        if points <= starting_points:
            starting_points -= points
            goodshots += 1
        else:
            badshots += 1
    elif shot == "Double":
        points *= 2
        if points <= starting_points:
            starting_points -= points
            goodshots += 1
        else:
            badshots += 1
    elif shot == "Triple":
        points *= 3
        if points <= starting_points:
            starting_points -= points
            goodshots += 1
        else:
            badshots += 1

if starting_points == 0:
    print(f"{player_name} won the leg with {goodshots} shots.")
