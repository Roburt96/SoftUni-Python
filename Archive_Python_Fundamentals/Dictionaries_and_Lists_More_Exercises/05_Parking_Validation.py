import re
plates = {}


def register_(name, plate, valid):
    if name in plates:
        print(f"ERROR: already registered with plate number {plates[name]}")

    elif not valid:
        print(f"ERROR: invalid license plate {plate}")

    elif valid:
        if any([True if plates[key] == plate else False for key in plates]):
            print(f"ERROR: license plate {plate} is busy")

        else:
            plates[name] = plate
            print(f"{name} registered {plate} successfully")


def unregister_(name):
    if name not in plates:
        print(f"ERROR: user {name} not found")
    else:
        print(f"user {name} unregistered successfully")
        del plates[name]



num_of_plates = int(input())
for i in range(num_of_plates):
    cmd, *info = [x for x in input().split()]

    if cmd == 'register':
        name = info[0]
        plate = info[1]
        pattern = (r"\b([A-Z]{2}[0-9]{4}[A-Z]{2})\b")
        check_valid = re.match(pattern, plate)
        register_(name, plate, check_valid)

    elif cmd == 'unregister':
        name = info[0]
        unregister_(name)

for key, value in plates.items():
    print(f"{key} => {value}")
