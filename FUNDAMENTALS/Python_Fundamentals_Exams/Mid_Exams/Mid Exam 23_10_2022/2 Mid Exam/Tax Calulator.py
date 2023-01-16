vehicle = input().split(">>")
total_sports_tax = 0
total_family_tax = 0
total_heavyduty_tax = 0
total_taxes = 0

for car in range(len(vehicle)):
    element = vehicle[car].split()
    years_tax = int(element[1])
    km_traveled = int(element[2])

    if 'family' in element[0]:
        initial_family_tax = 50
        discount_family_tax = years_tax * 5

        if km_traveled >= 3000:
            km_family_tax = (km_traveled // 3000) * 12
            total_family_tax += initial_family_tax - discount_family_tax + km_family_tax
            total_taxes += total_family_tax
            print(f"A {element[0]} car will pay {total_family_tax:.2f} euros in taxes.")
            total_family_tax = 0
        else:
            total_family_tax += initial_family_tax - discount_family_tax
            total_taxes += total_family_tax
            print(f"A {element[0]} car will pay {total_family_tax:.2f} euros in taxes.")
            total_family_tax = 0

    elif 'heavyDuty' in element[0]:
        initial_heavyduty_tax = 80
        discount_heavyduty_tax = years_tax * 8

        if km_traveled >= 9000:
            km_heavyduty_tax = (km_traveled // 9000) * 14
            total_heavyduty_tax += initial_heavyduty_tax - discount_heavyduty_tax + km_heavyduty_tax
            total_taxes += total_heavyduty_tax
            print(f"A {element[0]} car will pay {total_heavyduty_tax:.2f} euros in taxes.")
            total_heavyduty_tax = 0
        else:
            total_heavyduty_tax += initial_heavyduty_tax - discount_heavyduty_tax
            total_taxes += total_heavyduty_tax
            print(f"A {element[0]} car will pay {total_heavyduty_tax:.2f} euros in taxes.")
            total_heavyduty_tax = 0

    elif 'sports' in element[0]:
        initial_sports_tax = 100
        discount_sports_tax = years_tax * 9

        if km_traveled >= 2000:
            km_sports_tax = (km_traveled // 2000) * 18
            total_sports_tax += initial_sports_tax - discount_sports_tax + km_sports_tax
            total_taxes += total_sports_tax
            print(f"A {element[0]} car will pay {total_sports_tax:.2f} euros in taxes.")
            total_sports_tax = 0
        else:
            total_sports_tax += initial_sports_tax - discount_sports_tax
            total_taxes += total_sports_tax
            print(f"A {element[0]} car will pay {total_sports_tax:.2f} euros in taxes.")
            total_sports_tax = 0
    else:
        print("Invalid car type.")


print(f"The National Revenue Agency will collect {total_taxes:.2f} euros in taxes.")
