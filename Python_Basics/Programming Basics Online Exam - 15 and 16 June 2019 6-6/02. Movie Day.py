import math
time_for_photo = int(input())
number_of_scene = int(input())
time_for_one_scene = int(input())

terrain = time_for_photo * 0.15
time_for_scene = number_of_scene * time_for_one_scene
time_needed = terrain + time_for_scene

if time_for_photo < time_needed:
    print(f"Time is up! To complete the movie you need {math.ceil(time_needed - time_for_photo)} minutes.")
elif time_for_photo >= time_needed:
    print(f"You managed to finish the movie on time! You have {math.ceil(time_for_photo - time_needed)} minutes left!")
