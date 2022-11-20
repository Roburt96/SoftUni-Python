car_entry = set()

number_of_commands = int(input())
for i in range(number_of_commands):
    cmd, car_plate = input().split(", ")
    if 'IN' in cmd:
        car_entry.add(car_plate)
    elif 'OUT' in cmd:
        car_entry.remove(car_plate)


if car_entry:
    print("\n".join(car_entry))
else:
    print(f"Parking Lot is Empty")

