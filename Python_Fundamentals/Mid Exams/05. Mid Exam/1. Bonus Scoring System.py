# number_of_students = int(input())
# number_of_lectures = int(input())
# additional_bonus = int(input())
# new_attendance = 0
#
# for attend in range(1, number_of_students + 1):
#     attendance = int(input())
#     if attendance > new_attendance:
#         new_attendance = attendance
#
# total_bonus = new_attendance / number_of_lectures * (5 + additional_bonus)
#
# print(f"Max Bonus: {round(total_bonus)}.")
# print(f"The student has attended {new_attendance} lectures.")


number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
max_points = 0
new_attendance = 0

for attend in range(1, number_of_students + 1):
    attendance = int(input())
    total_bonus = attendance / number_of_lectures * (5 + additional_bonus)
    if attendance > new_attendance:
        max_points = total_bonus
        new_attendance = attendance


# total_bonus = new_attendance / number_of_lectures * (5 + additional_bonus)

print(f"Max Bonus: {round(max_points)}.")
print(f"The student has attended {new_attendance} lectures.")
