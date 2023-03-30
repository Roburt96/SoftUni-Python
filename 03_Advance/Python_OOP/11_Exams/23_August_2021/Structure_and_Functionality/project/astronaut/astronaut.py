from project.validator.validator import Validator
from abc import ABC, abstractmethod


class Astronaut(ABC):

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_name_is_empty_string(value)
        self.__name = value

    @abstractmethod
    def breathe(self):
        ...

    @abstractmethod
    def increase_oxygen(self, amount: int):
        ...