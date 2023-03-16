from project.validation.validator import Validator


class Player:
    all_players = set()

    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_for_empty_string(value, "Name not valid!")
        Validator.check_if_player_exist(value, Player.all_players)
        Player.all_players.add(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.check_player_is_under_12(value, "The player cannot be under 12 years old!")
        self.__age = value

    @property
    def need_sustenance(self):
        return self.stamina < 100

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        Validator.check_stamina_below_0_or_greater_100(value, "Stamina not valid!")
        self.__stamina = value

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
