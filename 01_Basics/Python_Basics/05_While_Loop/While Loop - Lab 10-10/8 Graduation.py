name = str(input())
excluded = 0
grade = 1
sum_graded = 0

while True:
    if excluded > 1:
        print(f"{name} has been excluded at {grade} grade")
        break
    score = float(input())

    if 4 <= score <= 6:
        sum_graded += score
        if grade == 12:
            print(f"{name} graduated. Average grade: {sum_graded / grade:.2f}")
            break
        grade += 1
    elif 2 <= score <= 4:
        excluded += 1
