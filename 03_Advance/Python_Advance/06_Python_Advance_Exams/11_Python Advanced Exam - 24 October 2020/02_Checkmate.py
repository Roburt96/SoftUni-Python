matrix = []
queen_list = []
king_r, king_c = 0, 0

for row in range(8):
    matrix.append(input().split())
    for col in range(8):
        if "Q" in matrix[row][col]:
            queen_list.append([row, col])
        if "K" in matrix[row]:
            king_r, king_c = row, matrix[row].index("K")

possition = ((1, 0),      # down
             (-1, 0),      # up
             (0, 1),      # right
             (0, -1),    # left
             (1, 1),    # down right
             (1, -1),   # down left
             (-1, -1),   # up left
             (-1, 1))    # up right

not_hit_king = True

for i in queen_list:
    c_row, c_col = i
    for row, col in possition:
        find = []
        for _ in range(8):
            c_row, c_col = c_row + row, c_col + col
            if 0 <= c_row <= 7 and 0 <= c_col <= 7:
                find.append(matrix[c_row][c_col])
                if "K" in find and "Q" not in find:
                    not_hit_king = False
                    print(i)
                    break
            else:
                break
        c_row, c_col = i

if not_hit_king:
    print("The king is safe!")









