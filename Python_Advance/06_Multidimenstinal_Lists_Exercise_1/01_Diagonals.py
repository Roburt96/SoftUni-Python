rows = int(input())
matrix = [[int(x) for x in input().split(",")]for _ in range(rows)]


def diagonals_(matrix, rows):
    diagonals_sum = {
        'Primary diagonal': [],
        'Secondary diagonal': []
    }

    for row in range(rows):
        diagonals_sum['Primary diagonal'].append(matrix[row][row])
        diagonals_sum['Secondary diagonal'].append(matrix[row][rows - row - 1])

    print(f"Primary diagonal: {', '.join(str(x) for x in diagonals_sum['Primary diagonal'])}. Sum: {sum(diagonals_sum['Primary diagonal'])}")
    print(f"Secondary diagonal: {', '.join(str(x) for x in diagonals_sum['Secondary diagonal'])}. Sum: {sum(diagonals_sum['Secondary diagonal'])}")


diagonals_(matrix, rows)
