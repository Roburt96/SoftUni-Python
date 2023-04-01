class Validator:

    @staticmethod
    def check_name_is_empty_string(name):
        if name == '' or name.isspace():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")

    @staticmethod
    def invalid_astronaut_type(astronaut_type: str):
        valid_types = ['Biologist', 'Geodesist', 'Meteorologist']
        if astronaut_type not in valid_types:
            raise Exception("Astronaut type is not valid!")

    @staticmethod
    def check_for_astronaut(name: str, astronauts: list):
        if all(name != astronaut.name for astronaut in astronauts):
            raise Exception(f"Astronaut {name} doesn't exist!")

    @staticmethod
    def check_planet_is_exist(p_name, planets: list):
        if all(p_name != planet.name for planet in planets):
            raise Exception("Invalid planet name!")

    @staticmethod
    def check_astronauts_for_mission(astronauts: list):
        if len(astronauts) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")