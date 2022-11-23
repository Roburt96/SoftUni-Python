initial_energy = int(input())
win_counter = 0
battle_won = True
command = input()
while command != "End of battle":
    command = int(command)
    if initial_energy - command >= 0:
        win_counter += 1
        initial_energy += - command
    else:
        battle_won = False
        break

    if win_counter % 3 == 0:
        initial_energy += win_counter
    command = input()

if battle_won:
    print(f"Won battles: {win_counter}.\n "
          f"Energy left: {initial_energy}")
else:
    print(f"No more energy! Game ends with {win_counter} won battles "
          f"and {initial_energy} energy")



