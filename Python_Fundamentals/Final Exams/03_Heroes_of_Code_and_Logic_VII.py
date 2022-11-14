number_Of_heroes = int(input())
heroes_info = {}

for i in range(number_Of_heroes):
    heroes = input()
    hero_name, HP, MP = heroes.split()

    heroes_info[hero_name] = heroes_info.get(hero_name, {'HP': 0, 'MP': 0})
    heroes_info[hero_name]['HP'] = int(HP)
    heroes_info[hero_name]['MP'] = int(MP)


def castspell_(name, mp_need, spell):
    if heroes_info[name]['MP'] >= mp_need:
        heroes_info[name]['MP'] -= mp_need
        print(f"{name} has successfully cast {spell} and now has {heroes_info[name]['MP']} MP!")
    elif heroes_info[name]['MP'] < mp_need:
        print(f"{name} does not have enough MP to cast {spell}!")


def takedamage_(name, damage, attacker):
    heroes_info[name]['HP'] -= damage
    if heroes_info[name]['HP'] > 0:
        print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes_info[name]['HP']} HP left!")
    else:
        print(f"{name} has been killed by {attacker}!")
        heroes_info.pop(name)


def recharge_(name, amount):
    max_mp = 200
    if heroes_info[name]['MP'] + amount > 200:
        print(f"{name} recharged for {200 - heroes_info[name]['MP']} MP!")
        heroes_info[name]['MP'] = max_mp
    else:
        heroes_info[name]['MP'] += amount
        print(f"{name} recharged for {amount} MP!")
    pass


def heal_(name, amount):
    max_hp = 100
    if heroes_info[name]['HP'] + amount > 100:
        print(f"{name} healed for {100 - heroes_info[name]['HP']} HP!")
        heroes_info[name]['HP'] = max_hp
    else:
        heroes_info[name]['HP'] += amount
        print(f"{name} healed for {amount} HP!")


commands = input()
while commands != 'End':
    cmd_type, *data = commands.split(" - ")

    if 'CastSpell' in cmd_type:
        name = data[0]
        MP_needed = int(data[1])
        spell_name = data[2]
        castspell_(name, MP_needed, spell_name)

    elif 'TakeDamage' in cmd_type:
        TD_name = data[0]
        damage = int(data[1])
        attacker = data[2]
        takedamage_(TD_name, damage, attacker)

    elif 'Recharge' in cmd_type:
        recharge_name = data[0]
        recharge_amount = int(data[1])
        recharge_(recharge_name, recharge_amount)

    elif 'Heal' in cmd_type:
        heal_name = data[0]
        heal_amount = int(data[1])
        heal_(heal_name, heal_amount)

    commands = input()


for name in heroes_info.keys():
    print(f"{name}")
    print(f"  HP: {heroes_info[name]['HP']}")
    print(f"  MP: {heroes_info[name]['MP']}")

# number_heroes = int(input())
#
# heroes_info = {}
#
#
# class Heroes:
#     def __init__(self, name):
#         self.name = name
#         self.hp = 0
#         self.mp = 0
#
#     def add_hp(self, hp):
#         self.hp += hp
#
#     def add_mp(self, mp):
#         self.mp += mp
#
#     def cast_spall(self, mp_need, spell_name):
#         if self.mp >= mp_need:
#             self.mp -= mp_need
#             return f"{self.name} has successfully cast {spell_name} and now has {self.mp} MP!"
#         return f"{self.name} does not have enough MP to cast {spell_name}!"
#
#     def take_damage(self, damage, attacker):
#         self.hp -= damage
#         if self.hp > 0:
#             return f"{self.name} was hit for {damage} HP by {attacker} and now has {self.hp} HP left!"
#         del heroes_info[self.name]
#         return f"{self.name} has been killed by {attacker}!"
#
#     def recharge(self, amount):
#         if self.mp + amount > 200:
#             amount = 200 - self.mp
#         self.mp += amount
#         return f"{self.name} recharged for {amount} MP!"
#
#     def heal(self, amount):
#         if self.hp + amount > 100:
#             amount = 100 - self.hp
#         self.hp += amount
#         return f"{self.name} healed for {amount} HP!"
#
#     def __repr__(self):
#         return f"{self.name}\n  " \
#                f"HP: {self.hp}\n  " \
#                f"MP: {self.mp}"
#
#
# for hero in range(number_heroes):
#     hero_name, hp, mp = [int(x) if x.isdigit() else x for x in input().split()]
#     heroes_info[hero_name] = heroes_info.get(hero_name, Heroes(hero_name))
#     heroes_info[hero_name].add_hp(hp)
#     heroes_info[hero_name].add_mp(mp)
#
# command = input()
#
# while command != "End":
#     command_type, hero_name, *info = [int(x) if x.isdigit() else x for x in command.split(" - ")]
#     if command_type == "Heal":
#         hp = info[0]
#         print(heroes_info[hero_name].heal(hp))
#     elif command_type == "Recharge":
#         mp = info[0]
#         print(heroes_info[hero_name].recharge(mp))
#     elif command_type == "TakeDamage":
#         damage, attacker = info
#         print(heroes_info[hero_name].take_damage(damage, attacker))
#     elif command_type == "CastSpell":
#         mp_need, spell_name = info
#         print(heroes_info[hero_name].cast_spall(mp_need, spell_name))
#
#     command = input()
#
# for hero in heroes_info.values():
#     print(hero)


