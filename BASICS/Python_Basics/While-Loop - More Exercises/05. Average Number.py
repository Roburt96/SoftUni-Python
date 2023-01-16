n = int(input())

total = 0

for i in range(1, n + 1):
    sum = int(input())
    total += sum / n
print(f"{total:.2f}")
