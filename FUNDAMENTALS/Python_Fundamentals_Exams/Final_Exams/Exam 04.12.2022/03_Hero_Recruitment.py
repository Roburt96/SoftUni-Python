
heroes = {}


def enroll_(name):
    if name in heroes:
        print(f"{name} is already enrolled.")
    else:
        heroes[name] = heroes.get(name, {'spellbook': []})


def learn_(name, spell):
    if name not in heroes:
        print(f"{name} doesn't exist.")
    elif spell in heroes[name]['spellbook']:
        print(f"{name} has already learnt {spell}.")
    else:
        heroes[name]['spellbook'].append(spell)


def unlearn_(name, spell):
    if name not in heroes:
        print(f"{name} doesn't exist.")
    elif spell not in heroes[name]['spellbook']:
        print(f"{name} doesn't know {spell}.")
    else:
        heroes[name]['spellbook'].remove(spell)

commands = input()
while commands != 'End':
    cmd_type, *data = commands.split()
    if 'Enroll' in cmd_type:
        hero_name = data[0]
        enroll_(hero_name)

    elif 'Learn' in cmd_type:
        hero_name = data[0]
        spell_name = data[1]
        learn_(hero_name, spell_name)

    elif 'Unlearn' in cmd_type:
        hero_name = data[0]
        spell_name = data[1]
        unlearn_(hero_name, spell_name)
    commands = input()

print('Heroes:')

for key in heroes.keys():
    print(f"== {key}: {', '.join(heroes[key]['spellbook'])}")