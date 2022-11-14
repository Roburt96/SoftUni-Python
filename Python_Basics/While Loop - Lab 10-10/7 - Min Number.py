inpt = input()
min = 10000000

while inpt != "Stop":
    num = int(inpt)

    if num < min:
        min = num
    inpt = input()

print(min)
