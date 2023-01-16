user_information = {'users': {}, "language": {}}

command = input()
while command != 'exam finished':
    name, *info = command.split("-")

    if 'banned' in info:
        username = name
        user_information['users'].pop(username)
    else:
        user_information['users'][name] = user_information['users'].get(name, 0)
        user_information["language"][info[0]] = user_information["language"].get(info[0], 0) + 1
        if user_information['users'][name] < int(info[1]):
            user_information['users'][name] = int(info[1])

    command = input()

print("Results:")
for items, values in user_information['users'].items():
    print(f"{items} | {values}")
print("Submissions:")
for key, counter in user_information['language'].items():
    print(f"{key} - {counter}")