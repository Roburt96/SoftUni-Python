from project.animal import Animal


class Tomcat(Animal):

    def __init__(self, name, age, gender="Male"):
        super().__init__(name, age, gender)

    def make_sound(self):
        return "Hiss"