from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):

    def __init__(self, name, oxygen=70):
        super().__init__(name, oxygen)

    @property
    def oxygen_take(self):
        return 5

    def breath(self):
        self.oxygen -= self.oxygen_take

    def increase_oxygen(self, amount: int):
        self.oxygen += amount