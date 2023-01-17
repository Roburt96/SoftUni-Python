rows, cols, names, score_board = 7, 7, input().split(", "), {}

for i in range(len(names)):
    score_board[names[i]] = score_board.get(names[i], {'score': 501, 'throw': 0})

matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(rows)]


while True:
    row, col = [int(x) for x in input()[1:-1].split(", ")]
    player = names[0]
    score_board[player]['throw'] += 1

    if row >= len(matrix) or col >= len(matrix):
        names.append(names.pop(0))
        continue

    if matrix[row][col] == "B":
        print(f"{player} won the game with {score_board[player]['throw']} throws!")
        break

    elif matrix[row][col] == 'D':
        total_sum = (matrix[row][0] + matrix[row][6] + matrix[0][col] + matrix[6][col]) * 2
        score_board[player]['score'] -= total_sum


    elif matrix[row][col] == 'T':
        total_sum = (matrix[row][0] + matrix[row][6] + matrix[0][col] + matrix[6][col]) * 3
        score_board[player]['score'] -= total_sum


    else:
        score_board[player]['score'] -= matrix[row][col]

    if score_board[player]['score'] <= 0:
        print(f"{player} won the game with {score_board[player]['throw']} throws!")
        break
    names.append(names.pop(0))






