move = {
    'left': {'row': 0, 'col': -1},
    'right': {'row': 0, 'col': 1},
    'up': {'row': -1, 'col': 0},
    'down': {'row': 1, 'col': 0}
}

initial = input()
size = int(input())
p_row, p_col = 0, 0

matrix = []

for row in range(size):
    matrix.append(list(input()))
    if 'P' in matrix[row]:
        p_row, p_col = row, matrix[row].index('P')
        matrix[p_row][p_col] = '-'


command_range = int(input())
for i in range(command_range):
    command = input()

    if move[command]:
        p_row, p_col = p_row + move[command]['row'], p_col + move[command]['col']

        if not 0 <= p_row < size or not 0 <= p_col < size:
            initial = initial[:-1]
            continue
        c_row, c_col = p_row, p_col
        if matrix[c_row][c_col] != '-':
            initial += matrix[c_row][c_col]
            matrix[c_row][c_col] = '-'

matrix[c_row][c_col] = 'P'
print(initial)
[print(*row, sep="") for row in matrix]
