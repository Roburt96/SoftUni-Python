directions = {
    'up': {'row': -1, 'col': 0},
    'down': {'row': 1, 'col': 0},
    'left': {'row': 0, 'col': -1},
    'right': {'row': 0, 'col': 1}
}

size_battlefield = int(input())
matrix = [[x for x in input()]for i in range(size_battlefield)]

map_info = {'battle_cruisers': 3, 'mine': 3}
current_row, current_col = 0, 0

for row in range(size_battlefield):
    for col in range(size_battlefield):
        if matrix[row][col] == 'S':
            current_row, current_col = row, col
            matrix[row][col] = "-"

while map_info['battle_cruisers'] and map_info['mine']:
    command = input()
    current_row, current_col = current_row + directions[command]['row'], current_col + directions[command]['col']

    if matrix[current_row][current_col] == "*":
        map_info['mine'] -= 1
        matrix[current_row][current_col] = "-"
    elif matrix[current_row][current_col] == "C":
        map_info['battle_cruisers'] -= 1
        matrix[current_row][current_col] = "-"

matrix[current_row][current_col] = 'S'

if not map_info['battle_cruisers']:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

elif not map_info['mine']:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{current_row}, {current_col}]!")

for i in matrix:
    print(*i, sep="")




