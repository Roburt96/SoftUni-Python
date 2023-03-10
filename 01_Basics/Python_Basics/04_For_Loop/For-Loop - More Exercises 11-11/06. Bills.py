month = int(input())
water = 20
internet = 15
other = 0

waterbills = 0
internetbill = 0
electricitybills = 0
otherbills = 0

for eng in range(1, month + 1):
    energy = float(input())

    electricitybills += energy
    waterbills += water
    internetbill += internet
    other = (energy + water + internet) * 1.2
    otherbills += other

average = (electricitybills + waterbills + internetbill + otherbills) / month
print(f"Electricity: {electricitybills:.2f} lv")
print(f"Water: {waterbills:.2f} lv")
print(f"Internet: {internetbill:.2f} lv")
print(f"Other: {otherbills:.2f} lv")
print(f"Average: {average:.2f} lv")
