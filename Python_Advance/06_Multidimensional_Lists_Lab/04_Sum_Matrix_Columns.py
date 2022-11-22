rows, columns = [int(x) for x in input().split(", ")]
matrix = []

for i in range(rows):
    elements = [int(x) for x in input().split()]
    matrix.append(elements)

for columns in range(columns):
    sum = 0
    for row in range(rows):
        sum += matrix[row][columns]
    print(sum)

