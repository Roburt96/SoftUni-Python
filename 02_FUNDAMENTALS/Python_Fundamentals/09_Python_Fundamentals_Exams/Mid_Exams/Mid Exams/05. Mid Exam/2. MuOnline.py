dungeon_room = input().split("|")
health = 100
bitcoins = 0
finish_dungeon = True

for room, command in enumerate(dungeon_room):
    command = command.split()
    type_command = command[0]
    points_command = command[-1]

    if type_command == "potion":
        if health + int(points_command) > 100:
            print(f"You healed for {100 - health} hp.")
            health = 100
        else:
            health += int(points_command)
            print(f"You healed for {points_command} hp.")
        print(f"Current health: {health} hp.")

    elif type_command == "chest":
        print(f"You found {points_command} bitcoins.")
        bitcoins += int(points_command)

    else:
        health -= int(points_command)

    if health > 0 and type_command != "potion" and type_command != "chest":
        print(f"You slayed {type_command}.")

    elif health <= 0:
        print(f"You died! Killed by {type_command}.")
        print(f"Best room: {room + 1}")
        finish_dungeon = False
        break


if finish_dungeon:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
