people = int(input())
capacity = int(input())


courses = people // capacity
people -= capacity * courses

if people > 0:
    people -= people
    courses += 1

print(courses)







