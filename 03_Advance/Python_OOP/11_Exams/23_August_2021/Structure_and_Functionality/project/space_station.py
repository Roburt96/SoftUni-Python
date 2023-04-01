from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository
from project.validator.validator import Validator


class SpaceStation:

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

        self.complete_mission = 0
        self.not_complete_mission = 0


    @property
    def get_astronaut(self):
        return {'Biologist': Biologist,
                'Geodesist': Geodesist,
                'Meteorologist': Meteorologist}

    def add_astronaut(self, astronaut_type: str, name: str):
        Validator.invalid_astronaut_type(astronaut_type)

        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        astronaut = self.get_astronaut[astronaut_type](name)
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."


    def add_planet(self, name: str, items: str):
        planet = Planet(name)
        current_items = [item.strip() for item in items.split(', ')]

        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        self.planet_repository.add(planet)
        for item in current_items:
            planet.items.append(item)
        return f"Successfully added Planet: {name}."


    def retire_astronaut(self, name: str):
        Validator.check_for_astronaut(name, self.astronaut_repository.astronauts)


        for pos, astro in enumerate(self.astronaut_repository.astronauts):
            if name == astro.name:
                del self.astronaut_repository.astronauts[pos]
                return f"Astronaut {name} was retired!"


    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        Validator.check_planet_is_exist(planet_name, self.planet_repository.planets)
        planet = [planet for planet in self.planet_repository.planets if planet.name == planet_name][0]
        suitable_astronauts = []

        for astronaut in sorted(self.astronaut_repository.astronauts, key=lambda astro: -astro.oxygen):
            if astronaut.oxygen > 30:
                suitable_astronauts.append(astronaut)

        Validator.check_astronauts_for_mission(suitable_astronauts)
        five_suitable_astronauts = [ast for ast in suitable_astronauts[:5]]

        for astro in five_suitable_astronauts:
            while planet.items and astro.oxygen > 0:
                astro.backpack.append(planet.items.pop())
                astro.breathe()

        if len(planet.items) == 0:
            self.complete_mission += 1
            return f"Planet: {planet_name} was explored. {len([astro for astro in suitable_astronauts if astro.backpack])} " \
                   f"astronauts participated in collecting items."

        self.not_complete_mission += 1
        return "Mission is not completed."

    def report(self):
        result = f"{self.complete_mission} successful missions!\n" \
                 f"{self.not_complete_mission} missions were not completed!\n" \
                 f"Astronauts' info:\n"

        for astronaut in self.astronaut_repository.astronauts:
            result += f"Name: {astronaut.name}\n" \
                      f"Oxygen: {astronaut.oxygen}\n"

            if astronaut.backpack:
                result += f"Backpack: {', '.join(astronaut.backpack)}\n"
            else:
                result += "Backpack items: none\n"

        return result






