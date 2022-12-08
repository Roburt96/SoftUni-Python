text = input()

commands = input()
while commands != 'End':
    cmd_type, *data = commands.split()

    if 'Translate' in cmd_type:
        char = data[0]
        replacement = data[1]
        text = text.replace(char, replacement)
        print(text)

    elif 'Includes' in cmd_type:
        substring = data[0]
        if substring in text:
            print("True")
        else:
            print("False")

    elif 'Start' in cmd_type:
        substring = data[0]
        if text.startswith(substring):
            print('True')
        else:
            print('False')

    elif 'Lowercase' in cmd_type:
        text = text.lower()
        print(text)

    elif 'FindIndex' in cmd_type:
        char = data[0]
        char_index = text.rindex(char)
        print(char_index)

    elif 'Remove' in cmd_type:
        startindex = int(data[0])
        endindex = int(data[1])
        text = text[:startindex] + text[startindex + endindex:]
        print(text)

    commands = input()
