movie = input()
kid = 0
standard = 0
student = 0
total_tickets = 0

while movie != "Finish":
    free_seats = int(input())
    busy_seats = 0

    for i in range(free_seats):
        ticket = input()
        if ticket == "kid":
            kid += 1
        elif ticket == "student":
            student += 1
        elif ticket == "standard":
            standard += 1
        elif ticket == "End":
            break
        total_tickets += 1
        busy_seats += 1

    percent_room = (busy_seats / free_seats) * 100
    total_tickets = kid + standard + student
    print(f"{movie} - {percent_room:.2f}% full.")

    movie = input()

percent_kid = (kid / total_tickets) * 100
percent_student = (student / total_tickets) * 100
percent_standard = (standard / total_tickets) * 100

print(f"Total tickets: {total_tickets}")
print(f"{percent_student:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kid:.2f}% kids tickets.")
