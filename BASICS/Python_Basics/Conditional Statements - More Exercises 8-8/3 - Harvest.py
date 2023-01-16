import math
X = int(input())   # loze
Y = float(input())  # grozde
Z = int(input())    # vino
workers = int(input())

grapes = X * Y
vine = (grapes * 0.40) / 2.5
vineremaining = abs(vine - Z)
vineworker = vineremaining / workers

if Z <= vine:
    print(f"Good harvest this year! Total wine: {math.floor(vine)} liters.")
    print(f"{math.floor(vineremaining)} liters left -> {math.floor(vineworker)} liters per person.")
else:
    print(f"It will be a tough winter! More {math.floor(vineremaining)} liters wine needed.")

