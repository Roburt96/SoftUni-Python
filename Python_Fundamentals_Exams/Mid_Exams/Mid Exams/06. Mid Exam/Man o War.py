def fire_(index, damage):
    global won_battle
    if 0 <= index < len(war_ship_status):
        war_ship_status[index] -= damage
        if war_ship_status[index] <= 0:
            won_battle = True


def defend_(start, end, damage):
    global lose_battle
    if 0 <= start_index < len(pirate_ship_status) and 0 <= end_index < len(pirate_ship_status):
        for dmg in range(start, end + 1):
            pirate_ship_status[dmg] -= damage
            if pirate_ship_status[dmg] <= 0:
                lose_battle = True


def repair_(index, hp):
    if 0 <= index < len(pirate_ship_status):
        pirate_ship_status[index] += hp
        if pirate_ship_status[index] > maximum_health_capacity:
            pirate_ship_status[index] = maximum_health_capacity


def status_():
    count_repair = 0

    for low in range(len(pirate_ship_status)):
        if pirate_ship_status[low] < lower_20_percent:
            count_repair += 1
    print(f"{count_repair} sections need repair.")


pirate_ship_status = [int(x) for x in input().split(">")]
war_ship_status = [int(x) for x in input().split(">")]
maximum_health_capacity = int(input())

won_battle = False
lose_battle = False
lower_20_percent = int(maximum_health_capacity * 0.20)

command = input()


while command != "Retire":
    command, *data = command.split()

    if "Fire" in command:
        index_f = int(data[0])
        damage = int(data[1])
        fire_(index_f, damage)

    elif "Defend" in command:
        start_index = int(data[0])
        end_index = int(data[1])
        damage = int(data[2])
        defend_(start_index, end_index, damage)

    elif "Repair" in command:
        index_r = int(data[0])
        health = int(data[1])
        repair_(index_r, health)

    elif "Status" in command:
        status_()

    if lose_battle:
        print("You lost! The pirate ship has sunken.")
        break

    elif won_battle:
        print("You won! The enemy ship has sunken.")
        break

    command = input()

pirate_hp = sum(pirate_ship_status)
war_hp = sum(war_ship_status)
if not won_battle and not lose_battle:
    print(f"Pirate ship status: {pirate_hp}")
    print(f"Warship status: {war_hp}")
