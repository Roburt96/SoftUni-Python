from collections import deque

firework = deque(int(x) for x in input().split(', '))
power = deque(int(x) for x in input().split(', '))

palm = 0
willow = 0
crossette = 0
is_perfect = False

while firework and power:
    if firework[0] <= 0:
        firework.popleft()
        continue
    if power[-1] <= 0:
        power.pop()
        continue

    current_firework = firework.popleft()
    current_power = power.pop()
    total = current_firework + current_power

    if total % 3 == 0 and total % 5 != 0:
        palm += 1
    elif total % 5 == 0 and total % 3 != 0:
        willow += 1
    elif total % 3 == 0 and total % 5 == 0:
        crossette += 1
    else:
        firework.append(current_firework - 1)
        power.append(current_power)

    if palm >= 3 and willow >= 3 and crossette >= 3:
        is_perfect = True
        break

if is_perfect:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework)}")
if power:
    print(f"Explosive Power left: {', '.join(str(x) for x in power)}")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {crossette}")