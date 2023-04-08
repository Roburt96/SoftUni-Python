from abc import abstractmethod, ABC

from project.validator.validator import Validator


class BaseRobot(ABC):

    def __init__(self, name: str, kind: str, price: float, weight: int):
        self.name = name
        self.kind = kind
        self.price = price
        self.weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.valid_name(value, "Robot name cannot be empty!")
        self.__name = value

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        Validator.valid_kind(value)
        self.__kind = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.valid_price(value)
        self.__price = value

    @abstractmethod
    def eating(self):
        ...