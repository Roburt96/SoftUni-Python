class Validator:

    @staticmethod
    def jockey_check_name(name):
        if name == "" or name.isspace():
            raise ValueError("Name should contain at least one character!")

    @staticmethod
    def jockey_check_age(age):
        if age < 18:
            raise ValueError("Jockeys must be at least 18 to participate in the race!")

    @staticmethod
    def horse_len_name(name):
        if len(name) < 4:
            raise ValueError(f"Horse name {name} is less than 4 symbols!")

    @staticmethod
    def horse_check_speed(speed, maximum_speed):
        if speed > maximum_speed:
            raise ValueError("Horse speed is too high!")

    @staticmethod
    def race_valid_types(value, valid_types):
        if value not in valid_types:
                raise ValueError("Race type does not exist!")

    @staticmethod
    def app_check_horse_exist(name, horse_list, message):
        if any(name == horse.name for horse in horse_list):
            raise Exception(message)

    @staticmethod
    def app_check_jockey_exist(name, jockey_list, message):
        if any(name == jockey.name for jockey in jockey_list):
            raise Exception(message)

    @staticmethod
    def app_check_race_exist(race_type, race_list, message):
        if any(race_type == r_type.race_type for r_type in race_list):
            raise Exception(message)

    @staticmethod
    def app_jockey_exist(name, jockey_list, message):
        if all(name != jockey.name for jockey in jockey_list):
            raise Exception(message)

    @staticmethod
    def app_horse_available(horse, horse_list, message):
        if all(h.is_taken for h in horse_list) or all(h.__class__.__name__ != horse for h in horse_list):
            raise Exception(message)



















