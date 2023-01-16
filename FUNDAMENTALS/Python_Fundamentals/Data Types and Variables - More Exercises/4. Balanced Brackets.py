n = int(input())
brackets = 0

for bracket in range(1, n + 1):
    text = input()
    if text == "(":
        brackets += 1
    elif text == ")":
        brackets -= 1
    if brackets != 0 and brackets != 1:
        print("UNBALANCED")
        break
else:
    print("BALANCED")

