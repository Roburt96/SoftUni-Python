from project.animals.animal import Bird
from project.food import Meat, Fruit, Vegetable, Seed

class Owl(Bird):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.owl_eat = [Meat]
        self.weight_increase = 0.25


    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.hen_eat = [Meat, Fruit, Vegetable, Seed]
        self.weight_increase = 0.35


    def make_sound(self):
        return "Cluck"

