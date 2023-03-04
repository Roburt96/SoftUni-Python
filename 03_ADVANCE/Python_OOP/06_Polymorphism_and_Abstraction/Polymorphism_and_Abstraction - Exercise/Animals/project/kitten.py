from project.animal import Animal


class Kitten(Animal):

    def __init__(self, name, age, gender="Female"):
        super().__init__(name, age, gender)

    def make_sound(self):
        return "Meow"