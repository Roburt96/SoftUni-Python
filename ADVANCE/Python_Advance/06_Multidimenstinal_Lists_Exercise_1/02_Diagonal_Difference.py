size = int(input())

matrix = [[int(x) for x in input().split()] for i in range(size)]
diagonals_sum = {
        'Primary diagonal': [],
        'Secondary diagonal': []
    }

for row in range(size):
    diagonals_sum['Primary diagonal'].append(matrix[row][row])
    diagonals_sum['Secondary diagonal'].append(matrix[row][size - row - 1])


difference = sum(diagonals_sum['Primary diagonal']) - sum(diagonals_sum['Secondary diagonal'])
print(abs(difference))