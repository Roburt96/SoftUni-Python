win_toy = {
    'Football': {'low': 100, 'high': 199},
    'Teddy Bear': {'low': 200, 'high': 299},
    'Lego Construction Set': {'low': 300, 'high': 399}
}
def find_buckets(rows, cols):
    global buckets_list
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "B":
                buckets_list.append([row, col])

def hit_target(row, col):
    global total_score, rows, cols
    if 0 <= row < rows and 0 <= col < cols:
        if matrix[row][col] == "B":
            matrix[row][col] = 0
            for r in range(rows):
                total_score += matrix[r][col]

def check_prize(score):
    global win_prize
    for key, value in win_toy.items():
        if value['low'] <= score <= value['high']:
            print(f"Good job! You scored {score} points, and you've won {key}.")
            win_prize = True
            break

total_score = 0
buckets_list = []
rows, cols = 6, 6
win_prize = False
matrix = [[int(x) if x.isdigit() else x for x in input().split()]for _ in range(rows)]
find_buckets(rows, cols)

for i in range(3):
    current_row, current_col = [int(x) for x in input()[1:-1].split(", ")]
    hit_target(current_row, current_col)

check_prize(total_score)

if not win_prize:
    print(f"Sorry! You need {abs(win_toy['Football']['low'] - total_score)} points more to win a prize.")