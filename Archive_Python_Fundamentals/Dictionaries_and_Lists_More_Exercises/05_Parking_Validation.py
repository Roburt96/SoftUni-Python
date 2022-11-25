import re
plates = {}


def register_(name, plate):
    if name in plates:
        print(f"ERROR: already registered with plate number {plate}")

        # print(f"ERROR: license plate {plate} is busy")
    else:
        plates[name] = plates.get(name, {'plate': plate})
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

    if 'register' in cmd:
        name = info[0]
        plate = info[1]
        pattern = (r"(?P<check>[A-Z]{2}[0-9]{4}[A-Z]{2})")
        check_valid = re.finditer(pattern, plate)

        if check_valid and len(plate) == 8:
            register_(name, plate)
        else:
            print(f"ERROR: invalid license plate {plate}")
            pass
    elif 'unregister' in cmd:
        name = info[0]
        unregister_(name)
