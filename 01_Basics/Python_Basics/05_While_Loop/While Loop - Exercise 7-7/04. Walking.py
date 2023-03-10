counter_steps = 0
goal = 10000


while True:
    steps = input()

    if steps == "Going home":
        steps = int(input())
        counter_steps += steps
        if counter_steps >= goal:
            print("Goal reached! Good job!")
            print(f"{abs(goal - counter_steps)} steps over the goal!")
        else:
            diff = goal - counter_steps
            print(f"{diff} more steps to reach goal.")
        break

    counter_steps += int(steps)

    if counter_steps >= goal:
        print("Goal reached! Good job!")
        print(f"{abs(goal - counter_steps)} steps over the goal!")
        break
