
from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat, Seed


class Mouse(Mammal):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.mouse_eat = [Vegetable, Fruit]
        self.weight_increase = 0.10

    def make_sound(self):
        return "Squeak"

class Dog(Mammal):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.dog_eat = [Meat]
        self.weight_increase = 0.40


    def make_sound(self):
        return "Woof!"

class Cat(Mammal):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.cat_eat = [Vegetable, Meat]
        self.weight_increase = 0.30


    def make_sound(self):
        return "Meow!"

class Tiger(Mammal):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.tiger_eat = [Meat]
        self.weight_increase = 1.00


    def make_sound(self):
        return "ROAR!!!"