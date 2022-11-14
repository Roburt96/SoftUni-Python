open_tabs = int(input())
salary = int(input())
Facebook = 150
Instagram = 100
Reddit = 50

for tabs in range(open_tabs):
    current_tabs = input()
    if current_tabs == "Facebook":
        salary -= Facebook
    elif current_tabs == "Instagram":
        salary -= Instagram
    elif current_tabs == "Reddit":
        salary -= Reddit

    if salary <= 0:
        break

if salary > 0:
    print(salary)
else:
    print("You have lost your salary.")
