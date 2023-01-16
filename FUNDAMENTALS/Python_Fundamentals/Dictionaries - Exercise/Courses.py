def courses_(key, name_student):
    if key not in courses_info:
        courses_info[key] = list()
        courses_info[key] = [str(name_student)]
    else:

        courses_info[key].append(name_student)


courses_info = {}

command = input()
while command != 'end':
    command = [x for x in command.split(" : ")]
    key_course = command[0]
    value_name = command[1]
    courses_(key_course, value_name)

    command = input()

value_students = 0


for k, v in courses_info.items():
    print(f"{k}: {len(v)}")
    for v in courses_info[k]:
        print(f"-- {''.join(v)}")
