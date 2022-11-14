def register_(reg_name, plate_number):
    if reg_name not in registered_car:
        registered_car[reg_name] = plate_number
        print(f"{reg_name} registered {plate_number} successfully")
    elif registered_car[reg_name]:
        print(f"ERROR: already registered with plate number {plate_number}")


def unregister_(unreg_name):
    if unreg_name in registered_car:
        registered_car.pop(unreg_name)
        print(f"{unreg_name} unregistered successfully")
    else:
        print(f"ERROR: user {unreg_name} not found")


registered_car = {}
number_of_cars = int(input())

for users in range(1, number_of_cars + 1):
    command, *plate = [x for x in input().split()]

    if command == 'register':
        reg_name = plate[0]
        plate_number = plate[1]
        register_(reg_name, plate_number)

    elif command == 'unregister':
        unreg_name = plate[0]
        unregister_(unreg_name)

for key, value in registered_car.items():
    print(f"{key} => {value}")

