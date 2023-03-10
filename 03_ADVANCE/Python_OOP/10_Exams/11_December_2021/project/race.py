from project.validator.validator import Validator


class Race:

    def __init__(self, name: str):
        self.name = name
        self.drivers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.empty_string(value)
        self.__name = value