information = input()

contest_info = {}


while information != 'no more time':
    information = information.split(' -> ')
    username = information[0]
    contest = information[1]
    user_points = int(information[2])
    contest_info[contest] = contest_info.get(contest, {})
    contest_info[contest][username] = contest_info[contest].get(username, 0)
    if contest_info[contest][username] < user_points:
        contest_info[contest][username] = user_points

    information = input()

point_sorted = {name: dict(sorted(course.items(), key=lambda x: (-x[1], x[0])))
                for name, course in contest_info.items()}


for name, students in point_sorted.items():
    print(f"{name}: {len(students)} participants")
    counter = 0
    for key, value in students.items():
        counter += 1
        print(f"{counter}. {key} <::> {value}")

print("Individual standings:")
new_list = {}
for key, value in contest_info.items():
    for user, point in value.items():
        if user not in new_list:
            new_list[user] = point
        else:
            new_list[user] += point
counter = 0
for key, value in sorted(new_list.items(), key=lambda x: (-x[1], x[0])):
    counter += 1
    print(f"{counter}. {key} -> {value}")



