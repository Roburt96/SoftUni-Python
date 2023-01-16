rows = int(input())
cols = rows
matrix = []

result = {}

b_row, b_col = 0, 0
start_row, start_col = 0, 0
directions = (
    ('up', -1, 0),
    ('down', 1, 0),
    ('left', 0, -1),
    ('right', 0, 1)
)
for row in range(rows):
    matrix.append([int(x) if x.isdigit() else x for x in input().split()])
    if "B" in matrix[row]:
        b_row, b_col = row, matrix[row].index("B")
        start_row, start_col = row, matrix[row].index("B")
        break


for move, row, col in directions:
    b_row, b_col = start_row, start_col
    num, cords = 0, []
    b_row, b_col = b_row + row, b_col + col
    for move_x in range(rows):
        if 0 <= b_row < rows and 0 <= b_col < cols and matrix[b_row][b_col] != "X":
            num += matrix[b_row][b_col]
            cords.append([b_row, b_col])
            b_row, b_col = row + b_row, col + b_col
        else:
            result[num] = {move: cords}
            break


if result != 0:
    best = max(result)
    for key, value in result[best].items():
        print(key)
        for i in value:
            print(i)
        print(best)




# 8
# 4 18 9 7 24 41 52 11
# 54 21 19 X 6 34 75 57
# 76 67 7 44 76 27 56 37
# 92 35 25 37 52 34 56 72
# 35 X 1 45 4 X 37 63
# 105 X B 2 12 43 5 19
# 48 19 35 20 32 27 42 4
# 73 88 78 32 37 52 X 22




