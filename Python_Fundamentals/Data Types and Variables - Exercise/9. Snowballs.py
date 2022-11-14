snowballs = int(input())

best_snowball = 0
best_weight = 0
best_time = 0
best_qualitiy = 0

for balls in range(snowballs):

    weight = int(input())
    time = int(input())
    quality = int(input())
    current_snowball = (weight / time) ** quality

    if balls == 0:
        best_snowball = current_snowball
        best_weight = weight
        best_time = time
        best_qualitiy = quality
    else:
        if current_snowball > best_snowball:
            best_snowball = current_snowball
            best_weight = weight
            best_time = time
            best_qualitiy = quality

print(f"{best_weight} : {best_time} = {int(best_snowball)} ({best_qualitiy})")
