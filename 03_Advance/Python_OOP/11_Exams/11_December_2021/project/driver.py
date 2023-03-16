from project.validator.validator import Validator


class Driver:

    def __init__(self, name: str):

        self.name = name
        self.car = None
        self.number_of_wins = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_for_empty_string_or_space(value)
        self.__name = value
