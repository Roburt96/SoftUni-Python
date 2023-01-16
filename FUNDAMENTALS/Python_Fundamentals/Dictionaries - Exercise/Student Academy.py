students_info = {}
high_grade = {}
int_num_of_pairs = int(input())
# grade_list = []
# current_name = ''
for _ in range(1, int_num_of_pairs * 2 + 1, 2):
    student_name = input()
    student_grade = float(input())
    # grade_list.append(student_grade)

    # if current_name != student_name:
    #     grade_list.clear()
    #     current_name = ''

    if student_name not in students_info:
        students_info[student_name] = list()
        students_info[student_name] = [float(student_grade)]
    else:
        students_info[student_name].append(float(student_grade))

for k, v in students_info.items():
    # average_sum = sum(v) / len(v)
    len_value = len(v)
    students_info[k] = sum(v) / len_value

for k, v in students_info.items():
    if students_info[k] >= 4.50:
        high_grade[k] = v

for k, v in high_grade.items():
    print(f"{k} -> {v:.2f}")

