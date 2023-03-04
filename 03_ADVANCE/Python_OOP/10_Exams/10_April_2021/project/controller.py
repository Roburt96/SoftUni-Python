from project.decoration.decoration_repository import DecorationRepository


class Controller:

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        ...

    def add_decoration(self, decoration_type: str):
        ...

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        ...

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        ...

    def feed_fish(self, aquarium_name: str):
        ...

    def calculate_value(self, aquarium_name: str):
        ...

    def report(self):
        ...







