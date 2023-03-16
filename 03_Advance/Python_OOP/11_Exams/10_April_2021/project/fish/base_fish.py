from abc import ABC, abstractmethod

from project.validation.validation import Validator


class BaseFish(ABC):

    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @abstractmethod
    def eat(self):
        ...

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_for_empty_string(value, "Fish name cannot be an empty string.")
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        Validator.check_for_empty_string(value, "Fish species cannot be an empty string.")
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.check_price_equal_or_below_zero(value, "Price cannot be equal to or below zero.")
        self.__price = value


