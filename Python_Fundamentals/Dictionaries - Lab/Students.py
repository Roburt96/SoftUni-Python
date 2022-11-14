students_info = input()
students_dict = {}


while not students_dict.get(students_info):
    students_info = students_info.split(":")
    name_student = students_info[0]
    id_student = students_info[1]
    course_student = students_info[-1]

    if course_student not in students_dict:
        students_dict[course_student] = {}
    students_dict[course_student][name_student] = id_student

    students_info = input()
    students_info = students_info.replace("_", " ")

for key, value in students_dict[students_info].items():
    print(f"{key} - {value}")


