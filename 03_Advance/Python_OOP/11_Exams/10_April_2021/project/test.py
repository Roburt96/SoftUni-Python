from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.controller import Controller
from project.fish.freshwater_fish import FreshwaterFish

fw = FreshwaterFish('roburt', 'ton', 3)
fa = FreshwaterAquarium('RobiAqua')
control = Controller()
fa.add_fish(fw)
control.add_aquarium('FreshwaterAquarium', 'roburt')

print(control.add_fish('roburt', 'FreshwaterFish', 'robifish', 'ton', 5))