tank_lenght = int(input())
tank_width = int(input())
tank_height = int(input())
percent = int(input())

volume_of_the_aquarium = tank_lenght * tank_width * tank_height
volume_in_liters = volume_of_the_aquarium / 1000
occupied_space = percent / 100

percent_liters = volume_in_liters * occupied_space
needed_liters =  volume_in_liters - percent_liters
print(needed_liters)
