n = int(input())

for i in range(1, n + 1):
    for j in range(1, n-i):
        print(end=" ")
    for j in range(1, n+1):
        print("*", end=" ")
    print()