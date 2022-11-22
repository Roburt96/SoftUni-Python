matrix_size = int(input())
matrix = []


for columns in range(matrix_size):
    elements = [int(x) for x in input().split()]
    matrix.append(elements)

sum = 0
for row in range(matrix_size):
    sum += matrix[row][row]
print(sum)

