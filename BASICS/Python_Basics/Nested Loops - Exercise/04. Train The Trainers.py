judges = int(input())
sum_grades = 0
total_grades = 0
average_grade = 0
counter = 0
name_presentation = input()
while True:
    counter += 1
    for i in range(judges):
        grade = float(input())
        sum_grades += grade
        average_grade = sum_grades / judges
    print(f"{name_presentation} - {average_grade:.2f}.")
    total_grades += average_grade
    sum_grades = 0

    name_presentation = input()
    if name_presentation == "Finish":
        break
total_grades_print = total_grades / counter
print(f"Student's final assessment is {total_grades_print:.2f}.")
