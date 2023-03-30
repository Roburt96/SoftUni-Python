from project.astronaut.astronaut_repository import AstronautRepository
from project.planet.planet_repository import PlanetRepository


class SpaceStation:

    def __init__(self):
        self.planet = PlanetRepository()
        self.astronaut = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        ...

    def add_planet(self, name: str, items: str):
        ...

    def retire_astronaut(self, name: str):
        ...

    def recharge_oxygen(self):
        ...

    def send_on_mission(self, planet_name: str):
        ...

    def report(self):
        ...







