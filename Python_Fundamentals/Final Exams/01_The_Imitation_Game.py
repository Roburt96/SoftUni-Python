encrypted_message = input()

command = input()

while command != 'Decode':
    cmd_type, *data = command.split('|')

    if 'Move' in cmd_type:
        num_of_letters = int(data[0])

        encrypted_message = encrypted_message[num_of_letters:] + encrypted_message[:num_of_letters]
    elif 'Insert' in cmd_type:
        index = int(data[0])
        value = data[1]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]

    elif 'ChangeAll' in cmd_type:
        substring = data[0]
        value = data[1]
        encrypted_message = encrypted_message.replace(substring, value)

    command = input()


print(f"The decrypted message is: {encrypted_message}")












