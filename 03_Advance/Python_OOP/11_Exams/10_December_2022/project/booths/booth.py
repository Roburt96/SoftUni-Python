from abc import ABC, abstractmethod

from project.validator.validator import Validator


class Booth(ABC):

    def __init__(self, booth_number: int, capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders = []
        self.price_for_reservation = 0.0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        Validator.booth_check_capacity_is_valid_number(value)
        self.__capacity = value

    @abstractmethod
    def reserve(self, number_of_people: int):
        ...

