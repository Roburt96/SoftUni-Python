materials = {
    "shards": 0,
    "fragments": 0,
    "motes": 0,
}

Shadowmourne = False
Valanyr = False
Dragonwrath = False

while not Shadowmourne and not Valanyr and not Dragonwrath:
    materials_input = input().lower().split()

    i = 1
    counter = 0

    for _ in range(int(len(materials_input) / 2)):
        current_material = materials_input[i]
        currency = int(materials_input[counter])
        materials[materials_input[i]] = materials.get(materials_input[i], 0) + currency

        i += 2
        counter += 2

        if materials["shards"] >= 250:
            Shadowmourne = True
            print(f"Shadowmourne obtained!")
            materials["shards"] -= 250
            break

        elif materials["fragments"] >= 250:
            Valanyr = True
            print(f"Valanyr obtained!")
            materials["fragments"] -= 250
            break

        elif materials["motes"] >= 250:
            Dragonwrath = True
            print(f"Dragonwrath obtained!")
            materials["motes"] -= 250
            break

for key, value in materials.items():
    print(f"{key}: {value}")





