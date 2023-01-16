password_reset = input()
password = []
command = input()
while command != 'Done':
    cmd_type, *data = command.split()

    if 'TakeOdd' in cmd_type:
        for pos, ele in enumerate(password_reset):
            if pos % 2:
                password.append(ele)
        password_reset = ''.join(password)
        print(password_reset)

    elif 'Cut' in cmd_type:
        index = int(data[0])
        length = int(data[1])
        password_reset = password_reset[:index] + password_reset[index + length:]
        print(password_reset)

    elif 'Substitute' in cmd_type:
        substring = data[0]
        substitute = data[1]
        if substring in password_reset:
            password_reset = password_reset.replace(substring, substitute)
            print(password_reset)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {password_reset}")
