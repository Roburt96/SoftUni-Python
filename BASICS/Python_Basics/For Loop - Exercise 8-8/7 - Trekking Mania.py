p1 = 0  #Musala
p2 = 0  #Monblan
p3 = 0  #Kilimndjaro
p4 = 0  #K2
p5 = 0  #Everest
numbers_of_group = int(input())
total_climbers = 0

for grp in range(numbers_of_group):
    group = int(input())
    total_climbers += group
    if group <= 5:
        p1 += group
    elif group <= 12:
        p2 += group
    elif group <= 25:
        p3 += group
    elif group <= 40:
        p4 += group
    else:
        p5 += group

print(f"{p1 / total_climbers * 100:.2f}%")
print(f"{p2 / total_climbers * 100:.2f}%")
print(f"{p3 / total_climbers * 100:.2f}%")
print(f"{p4 / total_climbers * 100:.2f}%")
print(f"{p5 / total_climbers * 100:.2f}%")
