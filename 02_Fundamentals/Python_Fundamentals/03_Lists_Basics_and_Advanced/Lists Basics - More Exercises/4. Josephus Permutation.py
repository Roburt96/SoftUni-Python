people_circle = input().split()
executed_step = int(input())
executed_people = []
number_of_people = len(people_circle)
position = executed_step - 1
index = 0

while number_of_people > 0:
    index = (position + index) % number_of_people
    executed_people.append(people_circle.pop(index))
    number_of_people -= 1

print(f"[{','.join(executed_people)}]")
