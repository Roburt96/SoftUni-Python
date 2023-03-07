class Validator:


    @staticmethod
    def check_for_empty_string(value, message_error):
        if value == "":
            raise ValueError(message_error)

    @staticmethod
    def check_equal_or_below_zero(value, message_error):
        if value <= 0:
            raise ValueError(message_error)

    @staticmethod
    def check_if_player_exist(value, all_players):
        if value in all_players:
            raise ValueError(f"Name {value} is already used!")

    @staticmethod
    def check_player_is_under_12(value, message_error):
        if value < 12:
            raise ValueError(message_error)

    @staticmethod
    def check_stamina_below_0_or_greater_100(value, message_error):
        if 0 > value > 100:
            raise ValueError(message_error)

    @staticmethod
    def check_no_food(value, list_food):
        if all(value != f.__class__.__name__ for f in list_food):
            raise ValueError("There are no food supplies left!")

    @staticmethod
    def check_no_drink(value, list_drink):
        if all(value != d.__class__.__name__ for d in list_drink):
            raise ValueError("There are no drink supplies left!")