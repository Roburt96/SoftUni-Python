move = {
    'left': {'row': 0, 'col': -1},
    'right': {'row': 0, 'col': 1},
    'up': {'row': -1, 'col': 0},
    'down': {'row': 1, 'col': 0}
}

size = int(input())

snake_row, snake_col, food_counter = 0, 0, 0
matrix = []
burrow_cords = []
win = False

for row in range(size):
    matrix.append(list(input()))
    if 'S' in matrix[row]:
        snake_row, snake_col = row, matrix[row].index('S')
        matrix[snake_row][snake_col] = '.'
    if 'B' in matrix[row]:
        burrow_cords.append([row, matrix[row].index('B')])


while True:
    command = input()

    if move[command]:
        snake_row, snake_col = snake_row + move[command]['row'], snake_col + move[command]['col']

        if not 0 <= snake_row < size or not 0 <= snake_col < size:
            print("Game over!")
            break
        if matrix[snake_row][snake_col] == '*':
            matrix[snake_row][snake_col] = '.'
            food_counter += 1

        elif matrix[snake_row][snake_col] == 'B':
            matrix[snake_row][snake_col] = '.'
            burrow_cords.remove([snake_row, snake_col])
            snake_row, snake_col = burrow_cords[0]
            matrix[snake_row][snake_col] = '.'

        else:
            matrix[snake_row][snake_col] = '.'

        if food_counter >= 10:
            win = True
            break


if win:
    matrix[snake_row][snake_col] = 'S'
    print("You won! You fed the snake.")

print(f"Food eaten: {food_counter}")
[print(*row, sep="") for row in matrix]