info = input()
phonebook = {}

while not info.isdigit():
    info = info.split("-")
    name = info[0]
    phone_number = info[1]

    if name not in phone_number:
        phonebook[name] = phone_number

    info = input()

for names in range(int(info)):
    name_exist = input()
    if name_exist in phonebook:
        print(f"{name_exist} -> {phonebook[name_exist]}")

    else:
        print(f"Contact {name_exist} does not exist.")
