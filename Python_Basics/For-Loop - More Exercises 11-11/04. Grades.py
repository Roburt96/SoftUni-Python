number_of_students = int(input())
average_rating = 0
student3to4 = 0
student4to5 = 0
top_student = 0
fail_student = 0

for students in range(1, number_of_students + 1):
    student_rating = float(input())
    if student_rating >= 5:
        average_rating += student_rating
        top_student += 1
    elif 4 <= student_rating <= 4.99:
        average_rating += student_rating
        student4to5 += 1
    elif 3 <= student_rating <= 3.99:
        average_rating += student_rating
        student3to4 += 1
    elif student_rating < 3:
        average_rating += student_rating
        fail_student += 1

average_rating = average_rating / number_of_students
# ok
percent = 100 / number_of_students
print(f"Top students: {percent * top_student:.2f}%")
print(f"Between 4.00 and 4.99: {percent*student4to5:.2f}%")
print(f"Between 3.00 and 3.99: {percent*student3to4:.2f}%")
print(f"Fail: {percent*fail_student:.2f}%")
print(f"Average: {average_rating:.2f}")
