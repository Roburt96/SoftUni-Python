from abc import ABC, abstractmethod

from project.validator.validator import Validator


class Delicacy(ABC):

    def __init__(self, name: str, portion: int, price: float):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.delicacy_check_valid_name(value)
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.delicacy_check_price_is_less_or_equal_zero(value)
        self.__price = value

    @abstractmethod
    def details(self):
       ...
