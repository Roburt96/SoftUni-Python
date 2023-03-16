class Validator:

    @staticmethod
    def car_model(model: str):
        if len(model) < 4:
            raise ValueError(f"Model {model} is less than 4 symbols!")

    @staticmethod
    def speed_limit(speed: int, speed_limit_min: int, speed_limit_max: int):
        if speed_limit_min > speed or speed > speed_limit_max:
            raise ValueError(f"Invalid speed limit! Must be between {speed_limit_min} and {speed_limit_max}!")

    @staticmethod
    def check_for_empty_string_or_space(value):
        if value == "" or value.isspace():
            raise ValueError("Name should contain at least one character!")

    @staticmethod
    def empty_string(value):
        if value == "":
            raise ValueError("Name cannot be an empty string!")

    @staticmethod
    def check_car_is_already_add(car, car_list: list):
        if any(car == c.model for c in car_list):
            raise Exception(f"Car {car} is already created!")

    @staticmethod
    def check_driver_is_already_add(driver, driver_list: list):
        if any(driver == d.name for d in driver_list):
            raise Exception(f"Driver {driver} is already created!")

    @staticmethod
    def check_race_is_already_add(race, race_list: list):
        if any(race == d.name for d in race_list):
            raise Exception(f"Race {race} is already created!")

    @staticmethod
    def check_driver_is_not_existing(driver, driver_list: list):
        if all(driver != d.name for d in driver_list):
            raise Exception(f"Driver {driver} could not be found!")

    @staticmethod
    def car_available(type_car: str, cars_list: list):
        if all(type_car == d.__class__.__name__ and d.is_taken for d in cars_list) or \
                all(type_car != d.__class__.__name__ for d in cars_list):
            raise Exception(f"Car {type_car} could not be found!")

    @staticmethod
    def controller_race_exists(race_name: str, race_list: list):
        if all(race_name != r.name for r in race_list):
            raise Exception(f"Race {race_name} could not be found!")

    @staticmethod
    def controller_driver_own_car(driver: object):
        if driver.car is None:
            raise Exception(f"Driver {driver.name} could not participate in the race!")

    @staticmethod
    def controller_race_participants(race: object):
        if len(race.drivers) < 3:
            raise Exception(f"Race {race.name} cannot start with less than 3 participants!")


