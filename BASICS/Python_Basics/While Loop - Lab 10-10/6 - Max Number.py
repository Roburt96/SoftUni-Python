inpt = input()
max = -10000000

while inpt != "Stop":
    num = int(inpt)

    if num > max:
        max = num
    inpt = input()

print(max)
