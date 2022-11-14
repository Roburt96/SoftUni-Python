houses = [int(x) for x in input().split("@")]
last_house = 0


def equal_0():
    houses[last_house] -= 2
    if houses[last_house] == 0:
        print(f"Place {last_house} has Valentine's day.")


def already_0():
    print(f"Place {last_house} already had Valentine's day.")


command = input()

while command != "Love!":
    command = command.split()
    command_type = command[0]
    jump_lenght = int(command[1])
    last_house += jump_lenght

    if last_house >= len(houses):
        last_house = 0

    if command_type == "Jump":
        if houses[last_house] == 0:
            already_0()

        elif houses[last_house] > 0:
            equal_0()

    command = input()

print(f"Cupid's last position was {last_house}.")

if sum(houses) == 0:
    print("Mission was successful.")

else:
    fail_times = [x for x in houses if x != 0]
    print(f"Cupid has failed {len(fail_times)} places.")
