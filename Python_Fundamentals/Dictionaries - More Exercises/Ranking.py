contest_and_password = input()
users_information = {"contest": {}, "students": {}}
contest_dict, students_dict = 'contest', 'students'

while contest_and_password != "end of contests":
    contest, password = contest_and_password.split(":")
    users_information[contest_dict][contest] = password

    contest_and_password = input()

user_input = input()
while user_input != 'end of submissions':
    contest, password, user, user_points = [int(x) if x.isdigit() else x for x in user_input.split("=>")]
    if contest in users_information[contest_dict] and users_information[contest_dict][contest] == password:
        users_information[students_dict][user] = users_information[students_dict].get(user, {})
        users_information[students_dict][user][contest] = users_information[students_dict][user].get(contest, 0)
        if users_information[students_dict][user][contest] < user_points:
            users_information[students_dict][user][contest] = user_points

    user_input = input()

best_user = ''
total_points = 0
for name_user in users_information[students_dict]:
    score_per_user = sum(users_information[students_dict][name_user].values())
    if score_per_user > total_points:
        total_points += score_per_user
        best_user = name_user
print(f"Best candidate is {best_user} with total {total_points} points.")
print("Ranking:")
for name in sorted(users_information[students_dict]):
    print(name)
    for key, value in sorted(users_information[students_dict][name].items(), key=lambda item: -item[-1]):
        print(f"#  {key} -> {value}")
