rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for i in range(rows)]
find = 0

for row in range(rows):
    for col in range(cols):
        if 0 <= row + 2 <= rows and 0 <= col + 2 <= cols:
            count = 0
            symbol = matrix[row][col]
            for row_check in range(row, row + 2):
                count += matrix[row_check][col:col + 2].count(symbol)
            if count == 4:
                find += 1

print(find)