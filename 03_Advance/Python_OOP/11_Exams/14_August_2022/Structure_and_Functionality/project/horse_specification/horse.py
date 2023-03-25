from abc import ABC, abstractmethod

from project.validator.validator import Validator


class Horse(ABC):

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken: bool = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.horse_len_name(value)
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        Validator.horse_check_speed(value, self.maximum_speed)
        self.__speed = value

    @abstractmethod
    def train(self):
        ...