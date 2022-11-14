number_Of_cars = int(input())
car_info = {}
for i in range(number_Of_cars):
    information = input()
    each_car = information.split("|")
    car = each_car[0]
    mileage = int(each_car[1])
    fuel = int(each_car[2])

    car_info[car] = car_info.get(car, {'mileage': mileage, 'fuel': fuel})


def drive_(car, distance, fuel):
    if car_info[car]['fuel'] > fuel:
        car_info[car]['mileage'] += distance
        car_info[car]['fuel'] -= fuel
        print(f"{car} driven for {distance} kilometers. "
              f"{fuel} liters of fuel consumed.")
    else:
        print("Not enough fuel to make that ride")

    if car_info[car]['mileage'] >= 100_000:
        print(f"Time to sell the {car}!")
        car_info.pop(car)


def refuel_(car, fuel):
    max_fuel = 75
    if car_info[car]['fuel'] + fuel > max_fuel:
        refuel = max_fuel - car_info[car]['fuel']
        car_info[car]['fuel'] += refuel
        print(f"{car} refueled with {refuel} liters")
    else:
        print(f"{car} refueled with {fuel} liters")
        car_info[car]['fuel'] += fuel


def revert_(car, km):
    car_info[car]['mileage'] -= km
    if car_info[car]['mileage'] >= 10_000:
        print(f"{car} mileage decreased by {km} kilometers")
    else:
       # car_info[car]['mileage'] < 10_000:
        car_info[car]['mileage'] = 10_000


commands = input()
while commands != 'Stop':
    cmd_type, *info = commands.split(" : ")

    if 'Drive' in cmd_type:
        car = info[0]
        distance = int(info[1])
        fuel = int(info[2])
        drive_(car, distance, fuel)

    elif 'Refuel' in cmd_type:
        car = info[0]
        fuel = int(info[1])
        refuel_(car, fuel)

    elif 'Revert' in cmd_type:
        car = info[0]
        kilometers = int(info[1])
        revert_(car, kilometers)

    commands = input()

for car in car_info.keys():
    print(f"{car} -> Mileage: {car_info[car]['mileage']} kms, Fuel in the tank: {car_info[car]['fuel']} lt.")

# car_numbers = int(input())
#
# car_info = {}
#
#
# class Car:
#
#     def __init__(self, name):
#         self.name = name
#         self.mileage = 0
#         self.fuel = 0
#
#     def add_mileage(self, mileage):
#         self.mileage += mileage
#
#     def add_fuel(self, fuel):
#         self.fuel += fuel
#
#     def drive(self, distance, fuel):
#         if self.fuel > fuel:
#             self.fuel -= fuel
#             self.mileage += distance
#             print(f"{self.name} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
#             if self.mileage >= 100_000:
#                 del car_info[self.name]
#                 print(f"Time to sell the {self.name}!")
#         else:
#             print("Not enough fuel to make that ride")
#
#     def refuel(self, fuel):
#         if self.fuel + fuel > 75:
#             fuel = 75 - self.fuel
#         self.fuel += fuel
#         print(f"{self.name} refueled with {fuel} liters")
#
#     def revert(self, kilometers):
#         self.mileage -= kilometers
#         if self.mileage < 10_000:
#             self.mileage = 10_000
#             return
#         print(f"{self.name} mileage decreased by {kilometers} kilometers")
#
#     def __repr__(self):
#         return f"{self.name} -> Mileage: {self.mileage} kms, Fuel in the tank: {self.fuel} lt."
#
#
# for car in range(car_numbers):
#     car_name, mileage, fuel = [int(x) if x.isdigit() else x for x in input().split("|")]
#     car_info[car_name] = car_info.get(car_name, Car(car_name))
#     car_info[car_name].add_mileage(mileage)
#     car_info[car_name].add_fuel(fuel)
#
# command = input()
#
# while command != "Stop":
#     command_type, car_name, *info = [int(x) if x.isdigit() else x for x in command.split(" : ")]
#     if command_type == "Drive":
#         distance, fuel = info
#         car_info[car_name].drive(distance, fuel)
#     elif command_type == "Refuel":
#         fuel = info[0]
#         car_info[car_name].refuel(fuel)
#     elif command_type == "Revert":
#         kilometers = info[0]
#         car_info[car_name].revert(kilometers)
#     command = input()
#
# for car in car_info.values():
#     print(car)
