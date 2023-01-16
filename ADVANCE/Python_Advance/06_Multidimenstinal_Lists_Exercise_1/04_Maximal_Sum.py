rows, cols = [int(x) for x in input().split()]
max_sum = -200
best = []
matrix = [[int(x) for x in input().split()] for i in range(rows)]


for row in range(rows):
    for col in range(cols):
        if 0 <= row + 3 <= rows and 0 <= col + 3 <= cols:
            current_best = []
            current_sum = 0
            for row_check in range(row, row + 3):
                current_best.append(matrix[row_check][col:col + 3])
                current_sum += sum(matrix[row_check][col:col + 3])
            if current_sum > max_sum:
                max_sum = current_sum
                best = current_best

print(f"Sum = {max_sum}")
[print(*row) for row in best]