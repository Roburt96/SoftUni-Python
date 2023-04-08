from abc import abstractmethod, ABC

from project.validator.validator import Validator


class BaseService(ABC):

    def  __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.robots = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.valid_name(value, "Service name cannot be empty!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        Validator.valid_capacity(value)
        self.__capacity = value

    def remove_capacity(self):
        self.capacity -= len(self.robots)

    @abstractmethod
    def details(self):
        ...

