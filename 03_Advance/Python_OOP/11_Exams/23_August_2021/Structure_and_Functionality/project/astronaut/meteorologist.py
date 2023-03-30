from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):

    def __init__(self, name, oxygen=90):
        super().__init__(name, oxygen)

    @property
    def oxygen_take(self):
        return 15

    def breathe(self):
        self.oxygen -= self.oxygen_take

    def increase_oxygen(self, amount: int):
        self.oxygen += amount