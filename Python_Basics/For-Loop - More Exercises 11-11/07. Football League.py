capacity = int(input())
number_of_fans = int(input())

a_sector = 0
b_sector = 0
v_sector = 0
g_sector = 0

for fans in range(1, number_of_fans + 1):
    sector = input()

    if sector == "A":
        a_sector += 1
    elif sector == "B":
        b_sector += 1
    elif sector == "V":
        v_sector += 1
    elif sector == "G":
        g_sector += 1

a_percent = (a_sector / number_of_fans) * 100
b_percent = (b_sector / number_of_fans) * 100
v_percent = (v_sector / number_of_fans) * 100
g_percent = (g_sector / number_of_fans) * 100
fan_percent = (number_of_fans / capacity) * 100

print(f"{a_percent:.2f}%")
print(f"{b_percent:.2f}%")
print(f"{v_percent:.2f}%")
print(f"{g_percent:.2f}%")
print(f"{fan_percent:.2f}%")
