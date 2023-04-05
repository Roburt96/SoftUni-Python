from abc import ABC, abstractmethod

from project.validator.validator import Validator


class Drink(ABC):

    @abstractmethod
    def __init__(self, name: str, portion: float, price: float, brand: str):
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_empty_string(value)
        self.__name = value

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value):
        Validator.check_portion_size(value)
        self.__portion = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        Validator.check_brand(value)
        self.__brand = value

    @abstractmethod
    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion}ml - {self.price:.2f}lv"