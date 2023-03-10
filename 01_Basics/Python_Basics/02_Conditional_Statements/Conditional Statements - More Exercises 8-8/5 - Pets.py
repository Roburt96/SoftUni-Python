import math
days = int(input())
food_in_kg = int(input())
food_for_dog = float(input())
food_for_cat = float(input())
food_for_turtle = float(input())

dog = days * food_for_dog
cat = days * food_for_cat
turtle = (days * food_for_turtle) / 1000
total_food = dog + cat + turtle
remainig = abs(math.ceil(total_food - food_in_kg))


if total_food <= food_in_kg:
    print(f"{remainig} kilos of food left.")
else:
    print(f"{remainig} more kilos of food are needed.")



