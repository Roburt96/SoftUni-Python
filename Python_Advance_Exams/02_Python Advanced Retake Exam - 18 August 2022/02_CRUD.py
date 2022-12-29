directions = {
    'up': {'row': -1, 'col': 0},
    'down': {'row': 1, 'col': 0},
    'left': {'row': 0, 'col': -1},
    'right': {'row': 0, 'col': 1}
}

matrix = [[x for x in input().split()]for _ in range(6)]
start_row, start_col = [int(x) for x in input()[1:-1].split(", ")]


command = input()
while command != "Stop":
    cmd, direct, *value = [x for x in command.split(", ")]
    cur_row, cur_col = [start_row + directions[direct]['row'], start_col + directions[direct]['col']]

    if cmd == 'Create':
        if matrix[cur_row][cur_col] == ".":
            matrix[cur_row][cur_col] = value[0]

    elif cmd == "Update":
        if matrix[cur_row][cur_col] != ".":
            matrix[cur_row][cur_col] = value[0]


    elif cmd == "Delete":
        if matrix[cur_row][cur_col].isalpha() or matrix[cur_row][cur_col].isdigit():
            matrix[cur_row][cur_col] = "."

    elif cmd == "Read":
        if matrix[cur_row][cur_col].isalpha() or matrix[cur_row][cur_col].isdigit():
            print(matrix[cur_row][cur_col])

    start_row, start_col = cur_row, cur_col
    command = input()

[print(*row) for row in matrix]


