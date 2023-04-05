from abc import ABC, abstractmethod

from project.validator.validator import Validator


class BakedFood(ABC):

    def __init__(self, name: str, portion: float, price: float):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_empty_string(value)
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.check_valid_price(value)
        self.__price = value

    @abstractmethod
    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"
