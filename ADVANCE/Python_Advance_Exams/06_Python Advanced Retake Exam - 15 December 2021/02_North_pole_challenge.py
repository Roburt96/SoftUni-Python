row, col = [int(x) for x in input().split(", ")]
matrix = []
cur_row, cur_col = 0, 0

items = {
    'Gifts': 0,
    'Cookies': 0,
    'Christmas decorations': 0
}

for rows in range(row):
    matrix.append(input().split())
    if "Y" in matrix[rows]:
        cur_row, cur_col = rows, matrix[rows].index("Y")

def check_items():
    result = 0
    for r in range(row):
        for c in range(col):
            if matrix[r][c] != "." and matrix[r][c] != 'x' and matrix[r][c] != 'Y':
                result += 1

command = input()
while command != 'End':
    cmd, steps = [int(x) if x.isdigit() else x for x in command.split("-")]

    while steps > 0:
        santa_row, santa_col = cur_row, cur_col
        matrix[santa_row][santa_col] = 'x'
        if cmd == "right":
            santa_col += 1
        elif cmd == "left":
            santa_col -= 1
        elif cmd == "up":
            santa_row -= 1
        elif cmd == "down":
            santa_row += 1
        steps -= 1
        if santa_row > row:
            santa_row = 0
        if santa_row < 0:
            santa_row = 5
        if santa_col > col:
            santa_col = 0
        if santa_col < 0:
            santa_col = 4

        if matrix[santa_row][santa_col] == "D":
            items['Christmas decorations'] += 1
            matrix[santa_row][santa_col] = "x"
        elif matrix[santa_row][santa_col] == "G":
            items['Gifts'] += 1
            matrix[santa_row][santa_col] = "x"
        elif matrix[santa_row][santa_col] == "C":
            items['Cookies'] += 1
            matrix[santa_row][santa_col] = "C"
        elif matrix[santa_row][santa_col] == ".":
            matrix[santa_row][santa_col] = 'x'
        elif matrix[santa_row][santa_col] == 'x':
            pass

        cur_row, cur_col = santa_row, santa_col
        [print(*row) for row in matrix]

    matrix[cur_row][cur_col] = 'Y'
    print()
    print()
    [print(*row) for row in matrix]




    command = input()


