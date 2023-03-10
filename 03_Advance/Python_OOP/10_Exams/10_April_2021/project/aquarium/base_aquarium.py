from abc import ABC, abstractmethod

from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish
from project.validation.validation import Validator


class BaseAquarium(ABC):

    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_for_empty_string(value, "Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        sum_comfort = sum([decoration.comfort for decoration in self.decorations])
        return sum_comfort

    def add_fish(self, fish: object):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."

        type_of_fish = fish.__class__.__name__

        if type_of_fish not in ["SaltwaterFish", "FreshwaterFish"]:
            return

        self.fish.append(fish)
        return f"Successfully added {type_of_fish} to {self.name}."

    def remove_fish(self, fish: object):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration: object):
        self.decorations.append(decoration)

    def feed(self):
        [f.eat() for f in self.fish]

    def __str__(self):
        result = [f"{self.name}" "Fish: "]
        if self.fish:
            result[1] += " ".join(f for f in self.fish)
        else:
            result[1] += "none"

        result.append(f"Decorations: {len(self.decorations)}\n"
                      f"Comfort: {self.calculate_comfort()}")

        return "\n".join(result)


