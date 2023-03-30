from abc import ABC

from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    def __init__(self, name, oxygen=50):
        super().__init__(name, oxygen)

    @property
    def oxygen_take(self):
        return 10

    def breath(self):
        self.oxygen -= self.oxygen_take

    def increase_oxygen(self, amount: int):
        self.oxygen += amount