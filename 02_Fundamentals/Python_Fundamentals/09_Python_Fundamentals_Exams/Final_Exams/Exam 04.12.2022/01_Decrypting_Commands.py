decrypthing = input()

commands = input()
while commands != 'Finish':
    cmd_type, *data = commands.split()
    if 'Replace' in cmd_type:
        current_char = data[0]
        new_char = data[1]
        decrypthing = decrypthing.replace(current_char, new_char)
        print(decrypthing)

    elif 'Make' in cmd_type:
        cmd = data[0]
        if cmd == 'Lower':
            decrypthing = decrypthing.lower()
            print(decrypthing)
        elif cmd == 'Upper':
            decrypthing = decrypthing.upper()
            print(decrypthing)

    elif 'Check' in cmd_type:
        check_string = data[0]
        if check_string in decrypthing:
            print(f"Message contains {check_string}")
        else:
            print(f"Message doesn't contain {check_string}")

    elif 'Sum' in cmd_type:
        startIndex = int(data[0])
        endIndex = int(data[1])
        if 0 < startIndex <= len(decrypthing) and 0 < endIndex <= len(decrypthing):
            if startIndex > 0 and endIndex > 0:
                sum_indexes = decrypthing[startIndex: endIndex + 1]
                total = 0
                for ch in range(len(sum_indexes)):
                    total += ord(sum_indexes[ch])
                print(total)
        else:
            print("Invalid indices!")

    elif 'Cut' in cmd_type:
        startindex = int(data[0])
        endindex = int(data[1])
        if 0 < startindex <= len(decrypthing) and 0 < endindex <= len(decrypthing):
            if startindex > 0 and endindex > 0:
                decrypthing = decrypthing[:startindex] + decrypthing[endindex + 1:]
                print(decrypthing)
        else:
            print("Invalid indices!")

    commands = input()