import math

serial = input()
number_of_seasons = int(input())
number_of_episodes = int(input())
episode_without_ad = float(input())

ad_total = episode_without_ad * 0.20

episode_with_ad = episode_without_ad + ad_total

bonus_time = number_of_seasons * 10

total_time = episode_with_ad * number_of_episodes * number_of_seasons + bonus_time

print(f"Total time needed to watch the {serial} series is {math.floor(total_time)} minutes.")
