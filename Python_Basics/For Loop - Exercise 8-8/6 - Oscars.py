actor_name = input()
academy_point = float(input())
number_judge = int(input())

for n in range(0, number_judge):
    judge_name = input()
    judge_points = float(input())
    lenght_name = len(judge_name)

    score = (lenght_name * judge_points) / 2

    academy_point += score

    if academy_point >= 1250.5:
        break

if academy_point >= 1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {academy_point:.1f}!')
else:
    needed_score = 1250.5 - academy_point
    print(f"Sorry, {actor_name} you need {needed_score:.1f} more!")
