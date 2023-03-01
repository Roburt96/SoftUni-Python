from project.animal import Animal


class Cheetah(Animal):

    def __init__(self, name, gender, age, money_for_care=60):
        super(Cheetah, self).__init__(name, gender, age, money_for_care)