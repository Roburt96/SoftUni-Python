from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race
from project.validator.validator import Validator


class Controller:

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    @property
    def __car_models(self):
        return {"SportsCar": SportsCar,
                "MuscleCar": MuscleCar}

    def __get_car(self, car):
        return [c for c in self.cars if car == c.__class__.__name__ and not c.is_taken][-1]

    def __get_driver(self, name):
        for d in self.drivers:
            if d.name == name:
                return d

    def __get_race(self, race):
        for r in self.races:
            if r.name == race:
                return r


    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.__car_models:
            return

        Validator.check_car_is_already_add(model, self.cars)
        car = self.__car_models[car_type](model, speed_limit)
        self.cars.append(car)
        return f"{car_type} {model} is created."


    def create_driver(self, driver_name: str):
        Validator.check_driver_is_already_add(driver_name, self.drivers)
        new_drivers = Driver(driver_name)
        self.drivers.append(new_drivers)
        return f"{driver_name} is created."

    def create_race(self, race_name: str):
        Validator.check_race_is_already_add(race_name, self.races)
        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        Validator.car_available(car_type, self.cars)
        Validator.check_driver_is_not_existing(driver_name, self.drivers)

        cur_name = self.__get_driver(driver_name)
        cur_car = self.__get_car(car_type)
        cur_car.is_taken = True

        if cur_name.car:
            old_model = cur_name.car
            old_model.is_taken = False
            cur_name.car = cur_car
            return f"Driver {driver_name} changed his car from {old_model.model} to {cur_car.model}."

        cur_name.car = cur_car
        return f"Driver {driver_name} chose the car {cur_name.car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        Validator.controller_race_exists(race_name, self.races)
        Validator.check_driver_is_not_existing(driver_name, self.drivers)

        current_driver = self.__get_driver(driver_name)
        Validator.controller_driver_own_car(current_driver)

        current_race = self.__get_race(race_name)
        if any(driver_name == d.name for d in current_race.drivers):
            return f"Driver {driver_name} is already added in {race_name} race."

        current_race.drivers.append(current_driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        Validator.controller_race_exists(race_name, self.races)

        current_race = self.__get_race(race_name)
        Validator.controller_race_participants(current_race)

        winners = [d for d in sorted(current_race.drivers, key=lambda x: -x.car.speed_limit)][:3]

        output = []
        for d in winners:
            d.number_of_wins += 1
            output.append(f"Driver {d.name} wins the {race_name} race with a speed of {d.car.speed_limit}.")

        return "\n".join(output)




