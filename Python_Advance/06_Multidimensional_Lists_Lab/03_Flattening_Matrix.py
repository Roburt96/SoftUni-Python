matrix_rows = int(input())
matrix = []
list_matrix = []

for i in range(matrix_rows):
    elements = list(map(int, input().split(", ")))
    matrix.append(elements)

list_matrix.append([x for flat_list in matrix for x in flat_list])
print(*list_matrix)