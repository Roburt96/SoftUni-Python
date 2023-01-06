from collections import deque
# ml_of_caffeine = deque([int(x) for x in input().split(", ")])
# energy_drinks = deque([int(x) for x in input().split(", ")])
# start = 0
#
# while ml_of_caffeine and energy_drinks:
#     current_caffeine = ml_of_caffeine.pop()
#     current_drink = energy_drinks.popleft()
#     total = current_caffeine * current_drink
#
#     if 300 >= start + total:
#         start += total
#         continue
#     else:
#         energy_drinks.append(current_drink)
#         start -= 30
#         if start < 0:
#             start = 0
#
#
#
# if len(energy_drinks) > 0:
#     print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
# else:
#     print(f"At least Stamat wasn't exceeding the maximum caffeine.")
#
# print(f"Stamat is going to sleep with {start} mg caffeine.")


class Drinks:

    def __init__(self, caffeine: deque, energy: deque):
        self.caffeine = deque(caffeine)
        self.energy = deque(energy)
        self.start = 0

    def check_(self):

        current_caffeine = self.caffeine.pop()
        current_energy = self.energy.popleft()
        total = current_caffeine * current_energy
        if 300 >= self.start + total:
            self.start += total

        else:
            self.energy.append(current_energy)
            self.start -= 30
            if self.start <= 0:
                self.start = 0

    def mg_caffeine(self):
        return f"Stamat is going to sleep with {self.start} mg caffeine."


ml_of_caffeine = deque(int(x) for x in input().split(", "))
energy_drinks = deque(int(x) for x in input().split(", "))
drink = Drinks(ml_of_caffeine, energy_drinks)
while drink.caffeine and drink.energy:
    drink.check_()

if len(drink.energy) > 0:
    print(f"Drinks left: {', '.join(str(x) for x in drink.energy)}")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(drink.mg_caffeine())