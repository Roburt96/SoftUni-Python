actor_name = input()
academy_points = float(input())
judges = int(input())


for total in range(0, judges):
    judge_name = input()
    judges_point = float(input())

    len_judge = len(judge_name)

    score = (len_judge * judges_point) / 2
    academy_points += score

    if academy_points >= 1250.5:
        break

if academy_points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {1250.5 - academy_points:.1f} more!")
