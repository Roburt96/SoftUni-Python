matrix_size = int(input())
matrix = []
find = False
for i in range(matrix_size):
    elements = [x for x in input()]
    matrix.append(elements)

symbol = input()

for row in range(matrix_size):
    if find:
        break
    for columns in range(matrix_size):
        if matrix[row][columns] == symbol:
            print(f"{row, columns}")
            find = True

if not find:
    print(f"{symbol} does not occur in the matrix")

