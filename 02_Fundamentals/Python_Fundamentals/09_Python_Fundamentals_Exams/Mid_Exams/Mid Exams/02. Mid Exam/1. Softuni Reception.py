employee_one = int(input())
employee_two = int(input())
employee_three = int(input())
students = int(input())
total_hour = 0
employees_answer_students_hour = employee_one + employee_two + employee_three


while students > 0:
    total_hour += 1
    if total_hour % 4 == 0:
        continue

    students -= employees_answer_students_hour
print(f"Time needed: {total_hour}h.")


