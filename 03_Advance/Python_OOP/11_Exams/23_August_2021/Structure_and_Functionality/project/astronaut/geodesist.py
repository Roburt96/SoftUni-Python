from abc import ABC

from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    def __init__(self, name):
        super().__init__(name, 50)

    def breath(self):
        self.oxygen -= 10

    def increase_oxygen(self, amount: int):
        self.oxygen += amount