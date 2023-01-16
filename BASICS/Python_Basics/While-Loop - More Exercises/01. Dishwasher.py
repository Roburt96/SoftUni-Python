bottles_of_detergent = int(input())
detergent = 750 * bottles_of_detergent
plates = 0
pots = 0
counter = 0

while detergent >= 0:
    command = input()

    if command == "End":
        break

    dishes = int(command)
    counter += 1

    if counter % 3 == 0:
        pots += dishes
        detergent -= pots * 15
    else:
        plates += dishes
        detergent -= dishes * 5

if detergent < 0:
    print(f"Not enough detergent, {-detergent} ml. more necessary!")
else:
    print(f"""Detergent was enough!
{plates} dishes and {pots} pots were washed.
Leftover detergent {detergent} ml.""")
