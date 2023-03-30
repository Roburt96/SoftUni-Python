from project.validator.validator import Validator


class Planet:

    def __init__(self, name: str):
        self.name = name
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_name_is_empty_string(value)
        self.__name = value