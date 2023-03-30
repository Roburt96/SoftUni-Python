from project.astronaut.astronaut import Astronaut


class AstronautRepository:

    def __init__(self):
        self.astronauts = []

    def __find_astronaut(self, name):
        for astronaut in self.astronauts:
            if astronaut.name == name:
                return astronaut

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name):
        return self.__find_astronaut(name)