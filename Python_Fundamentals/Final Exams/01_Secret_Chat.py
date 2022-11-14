concealed_message = input()

command = input()
while command != 'Reveal':
    cmd_type, *data = command.split(":|:")

    if 'InsertSpace' in cmd_type:
        index = int(data[0])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)

    elif 'Reverse' in cmd_type:
        substring = data[0]
        if substring in concealed_message:
            reverse_substring = substring[::-1]
            concealed_message = concealed_message.replace(substring, reverse_substring, 1)

            print(concealed_message)
        else:
            print('error')

    elif 'ChangeAll' in cmd_type:
        substring = data[0]
        replacement = data[1]
        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)

    command = input()

print(f"You have a new text message: {concealed_message}")
