# car_entry = set()
#
# number_of_commands = int(input())
# for i in range(number_of_commands):
#     cmd, car_plate = input().split(", ")
#     if 'IN' in cmd:
#         car_entry.add(car_plate)
#     elif 'OUT' in cmd:
#         car_entry.discard(car_plate)
#
#
# if car_entry:
#     print("\n".join(car_entry))
# else:
#     print(f"Parking Lot is Empty")


class Parking:

    def __init__(self):
        self.parking = set()

    def in_parking(self, plate):
        self.parking.add(plate)

    def out_parking(self, plate):
        self.parking.discard(plate)

    def returning(self):
        return self.parking


all_car = Parking()


def main():
    parking = all_car.returning()
    number_of_commands = int(input())
    for i in range(number_of_commands):
        cmd, car_plate = input().split(", ")
        if 'IN' in cmd:
            all_car.in_parking(car_plate)
        elif 'OUT' in cmd:
            all_car.out_parking(car_plate)

    if all_car.parking:
        print(*parking, sep="\n")
    else:
        print(f"Parking Lot is Empty")


main()









