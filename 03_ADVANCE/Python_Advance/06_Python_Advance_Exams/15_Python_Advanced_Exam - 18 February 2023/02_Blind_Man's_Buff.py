r, c = map(int, input().split())
matrix = []
p_row, p_col = 0, 0
move = 0
touch = 0
player_counter = 0

for row in range(r):
    matrix.append([x for x in input().split()])
    if 'B' in matrix[row]:
        p_row, p_col = row, matrix[row].index('B')

for row in range(r):
    for col in range(c):
        if matrix[row][col] == 'P':
            player_counter += 1

while True:
    command = input()
    if command == 'Finish':
        break

    if not player_counter:
        break

    cur_row, cur_col = p_row, p_col
    matrix[cur_row][cur_col] = '-'
    if command == 'up':
        cur_row, cur_col = p_row - 1, p_col

    elif command == 'down':
        cur_row, cur_col = p_row + 1, p_col

    elif command == 'left':
        cur_row, cur_col = p_row, p_col -1

    elif command == 'right':
        cur_row, cur_col = p_row, p_col + 1

    if cur_row < 0 or cur_row >= r or cur_col < 0 or cur_col >= c:
        continue

    if matrix[cur_row][cur_col] == 'O':
        continue
    elif matrix[cur_row][cur_col] == 'P':
        matrix[cur_row][cur_col] = 'B'
        p_row, p_col = cur_row, cur_col
        player_counter -= 1
        move += 1
        touch += 1
    elif matrix[cur_row][cur_col] == '-':
        matrix[cur_row][cur_col] = 'B'
        p_row, p_col = cur_row, cur_col
        move += 1



print('Game over!')
print(f"Touched opponents: {touch} Moves made: {move}")




