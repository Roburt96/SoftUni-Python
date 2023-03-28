from abc import ABC, abstractmethod

from project.validator.validator import Validator


class Meal(ABC):

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.valid_meal_name(value)
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.valid_meal_price(value)
        self.__price = value

    @abstractmethod
    def details(self):
        ...