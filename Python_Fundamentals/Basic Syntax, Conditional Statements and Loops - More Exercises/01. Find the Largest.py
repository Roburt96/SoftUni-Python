number = input()
sort = sorted(number, reverse=True)
for d, digit in enumerate(sort):
    print(digit, end="")
