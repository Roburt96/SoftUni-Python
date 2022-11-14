line = int(input())
capacity = 255
addwater = 0

for i in range(line):
    liters = int(input())
    if liters > capacity:
        print("Insufficient capacity!")
    else:
        capacity -= liters
        addwater += liters
print(addwater)




