people_waiting = int(input())
wagons = list(map(int, input().split(" ")))

for i in range(len(wagons)):
    max_people = min(4 - wagons[i], people_waiting)
    wagons[i] += max_people
    people_waiting -= max_people

if people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a "
          f"queue!")
elif len([wagon for wagon in wagons if wagon < 4]) > 0:
    print(f"The lift has empty spots!")

print(" ".join([str(wagon) for wagon in wagons]))







