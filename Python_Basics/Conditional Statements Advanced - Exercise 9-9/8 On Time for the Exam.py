exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

total_exam_minutes = exam_hour * 60 + exam_minutes
total_arrival_minutes = arrival_hour * 60 + arrival_minutes
left_hour = 0
left_minutes = 0

difference = abs(total_exam_minutes - total_arrival_minutes)

if total_arrival_minutes > total_exam_minutes:
    print("Late")
    if difference >= 60:
        left_hour = difference // 60
        left_minutes = difference % 60
        if left_minutes < 10:
            print(f"{left_hour}:0{left_minutes} hours after the start")
        else:
            print(f"{left_hour}:{left_minutes} hours after the start")
    else:
        if difference < 10:
            print(f"{difference} minutes after the start")
        else:
            print(f"{difference} minutes after the start")
elif total_exam_minutes == total_arrival_minutes:
    print("On time")
elif total_arrival_minutes < total_exam_minutes:
    if difference <= 30:
        print("On time")
        print(f"{difference} minutes before the start")
    else:
        if difference >= 60:
            left_hour = difference // 60
            left_minutes = difference % 60
            if left_minutes < 10:
                print("Early")
                print(f"{left_hour}:0{left_minutes} hours before the start")
            else:
                print("Early")
                print(f"{left_hour}:{left_minutes} hours before the start")
        else:
            print("Early")
            print(f"{difference} minutes before the start")
