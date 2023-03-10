n1 = int(input())
n2 = int(input())
n3 = int(input())

for num1 in range(2, n1 + 1, 2):
    for num2 in range(2, n2 + 1):
        for num3 in range(2, n3 + 1, 2):
            if num2 == 2 or num2 == 3 or num2 == 5 or num2 == 7:
                print(f"{num1} {num2} {num3}")
