
spell = input()
command = input()
while command != 'Abracadabra':
    cmd_type, *data = command.split()
    if cmd_type == 'Abjuration':
        spell = spell.upper()
        print(spell)

    elif cmd_type == 'Necromancy':
        spell = spell.lower()
        print(spell)

    elif cmd_type == 'Illusion':
        index = int(data[0])
        letter = data[1]
        if 0 > index > len(spell):
            print('The spell was too weak.')
        else:
            spell = spell[:index] + letter + spell[index+1:]
            print('Done')

    elif cmd_type == 'Divination':
        first_sub = data[0]
        second_sub = data[1]
        if first_sub in spell:
            spell = spell.replace(first_sub, second_sub)
            print(spell)

    elif cmd_type == 'Alteration':
        substring = data[0]
        if substring in spell:
            spell = spell.replace(substring, '')
            print(spell)

    else:
        print('The spell did not work!')
    command = input()
