moves = int(input())
score = 0
interval1 = 0
interval2 = 0
interval3 = 0
interval4 = 0
interval5 = 0
interval6 = 0

for move in range(1, moves + 1):
    number = int(input())

    if 0 <= number <= 9:
        score += (number * 0.2)
        interval1 += 1
    elif 10 <= number <= 19:
        score += (number * 0.3)
        interval2 += 1
    elif 20 <= number <= 29:
        score += (number * 0.4)
        interval3 += 1
    elif 30 <= number <= 39:
        score += 50
        interval4 += 1
    elif 40 <= number <= 50:
        score += 100
        interval5 += 1
    else:
        score = score / 2
        interval6 += 1


percent = 100 / moves
print(f"{score:.2f}")
print(f"From 0 to 9: {interval1 * percent:.2f}%")
print(f"From 10 to 19: {interval2 * percent:.2f}%")
print(f"From 20 to 29: {interval3 * percent:.2f}%")
print(f"From 30 to 39: {interval4 * percent:.2f}%")
print(f"From 40 to 50: {interval5 * percent:.2f}%")
print(f"Invalid numbers: {interval6 * percent:.2f}%")
