# grams
food_in_gr = float(input()) * 1000
hay_in_gr = float(input()) * 1000
cover_in_gr = float(input()) * 1000
guinea_weight = float(input()) * 1000
total_food = food_in_gr
total_hay = hay_in_gr
total_cover = cover_in_gr
no_food = False

for day in range(1, 31):
    total_food -= 300
    if day % 2 == 0:
        total_hay -= total_food * 0.05
    if day % 3 == 0:
        total_cover -= guinea_weight / 3

    if total_food < 0 or total_hay < 0 or total_cover < 0:
        no_food = True
        break

if no_food:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {total_food/1000:.2f}, "
          f"Hay: {total_hay/1000:.2f}, Cover: {total_cover/1000:.2f}.")







