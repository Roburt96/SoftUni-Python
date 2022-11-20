number_of_students = int(input())
student_record = {}

for i in range(number_of_students):
    name, grade = [float(x) if x[-1].isdigit() else x for x in input().split()]
    student_record[name] = student_record.get(name, []) + [grade]

for name, score in student_record.items():
    avg_grade = sum(score) / len(score)
    print(f"{name} -> {' '.join(f'{grades:.2f}' for grades in score)} (avg: {avg_grade:.2f})")

