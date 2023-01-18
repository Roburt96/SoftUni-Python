move = {
    'left': {'row': 0, 'col': -1},
    'right': {'row': 0, 'col': 1},
    'up': {'row': -1, 'col': 0},
    'down': {'row': 1, 'col': 0}
}

size = int(input())
p_row, p_col = 0, 0
matrix = []
coins = 0
path  = []
win = False

for row in range(size):
    matrix.append([int(x) if x.isdigit() else x for x in input().split()])
    if "P" in matrix[row]:
        p_row, p_col = row, matrix[row].index('P')
        path.append([p_row, p_col])
        matrix[p_row][p_col] = '.'


while True:
    move_command = input()

    if move[move_command]:
        p_row, p_col = p_row + move[move_command]['row'], p_col + move[move_command]['col']

        if p_row < 0:
            p_row = size - 1
        if p_row > size - 1:
            p_row = 0
        if p_col < 0:
            p_col = size - 1
        if p_col > size - 1:
            p_col = 0
        path.append([p_row, p_col])
        if matrix[p_row][p_col] == "X":
            coins = round(coins * 0.5)
            break

        elif matrix[p_row][p_col] == ".":
            continue

        else:
            coins += matrix[p_row][p_col]
            matrix[p_row][p_col] = "."

    if coins >= 100:
        win = True
        break


if not win:
    print(f"Game over! You've collected {coins} coins.")
else:
    print(f"You won! You've collected {coins} coins.")
print('Your path:')
print('\n'.join(str(x) for x in path))
