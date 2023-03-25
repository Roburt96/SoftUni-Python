from project.validator.validator import Validator


class HorseRace:

    def __init__(self, race_type: str):
        self.race_type = race_type
        self.jockeys = []

    @property
    def __valid_types(self):
        return ["Winter", "Spring", "Autumn", "Summer"]

    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value):
        Validator.race_valid_types(value, self.__valid_types)
        self.__race_type = value