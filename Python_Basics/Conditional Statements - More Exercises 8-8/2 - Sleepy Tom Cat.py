import math

days = int(input())
normalplay = 30000
restdays = days * 127
workdays = 365 - days
playworkdays = workdays * 63
playtime = restdays + playworkdays
totalplaytime = abs(normalplay - playtime)

hours = totalplaytime // 60
minutes = totalplaytime % 60

if normalplay > playtime:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")








