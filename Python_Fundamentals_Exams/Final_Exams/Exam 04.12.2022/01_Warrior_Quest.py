skills = input()

commands = input()

while commands != 'For Azeroth':
    cmd = commands.split()
    if cmd[0] == 'GladiatorStance':
        skills = skills.upper()
        print(skills)

    elif cmd[0] == 'DefensiveStance':
        skills = skills.lower()
        print(skills)

    elif cmd[0] == 'Dispel':
        index = int(cmd[1])
        letter = cmd[2]

        if 0 > index >= len(skills):
            print("Dispel too weak.")
        else:
            skills = skills[:index] + letter + skills[index+1:]
            print("Success!")

    elif 'Target Change' in commands:
        first_substring = cmd[2]
        second_substring = cmd[3]
        if first_substring not in skills:
            print(skills)
        else:
            skills = skills.replace(first_substring, second_substring)
            print(skills)

    elif 'Target Remove' in commands:
        substring = cmd[2]
        if substring in skills:
            skills = skills.replace(substring, '')
            print(skills)

    elif 'Target Change' not in commands or 'Target Remove' not in commands or cmd[0] != 'GladiatorStance' \
            or cmd[0] != 'DefensiveStance' or cmd[0] != 'Dispel':
        print("Command doesn't exist!")


    commands = input()

