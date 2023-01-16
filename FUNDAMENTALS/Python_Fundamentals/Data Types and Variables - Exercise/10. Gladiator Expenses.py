lost_fights = int(input())
helm_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helm = 0
sword = 0
shield = 0
armor = 0

for lost in range(1, lost_fights + 1):
    if lost % 2 == 0:
        helm += 1
    if lost % 3 == 0:
        sword += 1

        if lost % 3 == 0 and lost % 2 == 0:
            shield += 1
            if shield % 2 == 0:
                armor += 1

total = helm_price * helm + sword_price * sword + shield_price * shield + armor_price * armor
print(f"Gladiator expenses: {total:.2f} aureus")