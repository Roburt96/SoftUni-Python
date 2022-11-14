import math

movie = input()
episode = int(input())
lunch_break = int(input())

lunch = lunch_break * 1/8
free_time = lunch_break * 1/4
time_left = lunch_break - lunch - free_time



if time_left >= episode:
    print(f"You have enough time to watch {movie} and left with {math.ceil(time_left - episode)} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie}, you need {math.ceil(episode - time_left)} more minutes.")
    