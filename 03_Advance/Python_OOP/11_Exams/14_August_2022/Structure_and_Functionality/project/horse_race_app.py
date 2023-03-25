from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey
from project.validator.validator import Validator


class HorseRaceApp:

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    @property
    def __horse_type(self):
        return {"Appaloosa": Appaloosa,
                "Thoroughbred": Thoroughbred}

    def find_jockey(self, name):
        for jockey in self.jockeys:
            if jockey.name == name:
                return jockey


    def find_horse(self, horse_type):
        h = next(
            filter(lambda x: (type(x).__name__ == horse_type and not x.is_taken), reversed(self.horses)),
            None)
        if not h:
            raise Exception("Horse breed {horse_type} could not be found!")
        return h

    def find_horse_race(self, race_type):
        found_race = next(filter(lambda x: x.race_type == race_type, self.horse_races), None)
        if not found_race:
            raise Exception(f"Race {race_type} could not be found!")
        return found_race

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        Validator.app_check_horse_exist(horse_name, self.horses, f"Horse {horse_name} already exists!")
        if horse_type in self.__horse_type:
            horse = self.__horse_type[horse_type](horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        Validator.app_check_jockey_exist(jockey_name, self.jockeys, f"Jockey {jockey_name} has been already added!")
        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        Validator.app_check_race_exist(race_type, self.horse_races, f"Race {race_type} has been already created!")
        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        Validator.app_horse_available(horse_type, self.horses, f"Horse breed {horse_type} could not be found!")
        Validator.app_jockey_exist(jockey_name, self.jockeys, f"Jockey {jockey_name} could not be found!")
        horse = self.find_horse(horse_type)
        jockey = self.find_jockey(jockey_name)

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f'Jockey {jockey_name} will ride the horse {horse.name}.'

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):

        race = self.find_horse_race(race_type)
        jockey = self.find_jockey(jockey_name)

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if any(j.name == jockey_name for j in race.jockeys):
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.find_horse_race(race_type)

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        fastest_jockey = sorted(race.jockeys, key=lambda jockey: -jockey.horse.speed)[0]
        return f'The winner of the {race_type} race, with a speed of {fastest_jockey.horse.speed}km/h ' \
               f'is {fastest_jockey.name}! Winner\'s horse: {fastest_jockey.horse.name}.'

















