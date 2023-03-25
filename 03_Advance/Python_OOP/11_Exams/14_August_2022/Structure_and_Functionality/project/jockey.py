from project.validator.validator import Validator


class Jockey:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.horse = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.jockey_check_name(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.jockey_check_age(value)
        self.__age = value
