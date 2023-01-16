num = [int(number) for number in input().split()]

for i in range(len(num)):
    if num[i] < 0:
        num[i] = abs(num[i])
    elif num[i] > 0:
        num[i] = -abs(num[i])

print(sum)