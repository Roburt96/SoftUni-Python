matrix = []
white_row, white_col = 0, 0
black_row, black_col = 0, 0

for row in range(8):
    matrix.append(input().split())
    if 'b' in matrix[row]:
        black_row, black_col = row, matrix[row].index('b')
    if 'w' in matrix[row]:
        white_row, white_col = row, matrix[row].index('w')


while True:
    if (white_row - 1, white_col -1) == (black_row, black_col) or (white_row - 1, white_col + 1) == (black_row, black_col):
        print(f"Game over! White win, capture on {chr(97 + black_col)}{abs(black_row - 8)}.")
        break
    white_row -= 1
    if white_row == -1:
        print(f"Game over! White pawn is promoted to a queen at {chr(97 + white_col)}8.")
        break

    if (black_row + 1, black_col - 1) == (white_row, white_col) or (black_row + 1, black_col + 1) == (white_row, white_col):
        print(f"Game over! Black win, capture on {chr(97 + white_col)}{abs(white_row - 8)}.")
        break
    black_row += 1
    if black_row == 8:
        print(f"Game over! Black pawn is promoted to a queen at {chr(97 + black_col)}1.")
        break
