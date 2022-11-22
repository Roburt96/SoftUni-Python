matrix_rows = int(input())
matrix = []

# for i in range(matrix_rows):
#     elements_even = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
#     matrix.append(elements_even)
#
# print(matrix)

for i in range(matrix_rows):
    elements = list(map(int, input().split(", ")))
    matrix.append(elements)
matrix = [[x for x in elements if x % 2 == 0] for elements in matrix]
print(matrix)