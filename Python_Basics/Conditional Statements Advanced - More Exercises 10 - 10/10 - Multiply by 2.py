num = float(input())
sum = 0

while True:
    if num < 0:
        print("Negative number!")
        break
    sum = num * 2
    print(f"Result: {sum:.2f}")
    num = float(input())
