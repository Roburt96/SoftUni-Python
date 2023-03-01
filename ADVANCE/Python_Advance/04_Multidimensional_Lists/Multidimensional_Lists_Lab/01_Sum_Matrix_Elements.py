rows, columns = [int(x) for x in input().split(", ")]
matrix = []
total_sum = 0
for i in range(rows):
    numbers = [int(x) for x in input().split(", ")]
    matrix.append(numbers)

for total in range(len(matrix)):
    total_sum += sum(matrix[total])

print(total_sum)
print(matrix)