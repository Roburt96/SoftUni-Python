from project.validation.validator import Validator


class Controller:

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        already_added_players = []
        for pl in players:
            if pl not in self.players:
                already_added_players.append(pl.name)
                self.players.append(pl)

        return f"Successfully added: {', '.join(str(x) for x in already_added_players)}"

    def add_supply(self, supplies):
        [self.supplies.append(s) for s in supplies]

    def __check_player(self, name: str):
        for p_name in self.players:
            if p_name.name == name:
                return p_name

    def __check_supply(self, name):
        return [(pos, supply) for pos, supply in enumerate(self.supplies) if supply.__class__.__name__ == name][-1]

    def sustain(self, player_name: str, sustenance_type: str):
        if all(p.name != player_name for p in self.players) or sustenance_type not in ("Food", "Drink"):
            return

        player = self.__check_player(player_name)
        if sustenance_type == "Food":
            Validator.check_no_food(sustenance_type, self.supplies)
        elif sustenance_type == "Drink":
            Validator.check_no_drink(sustenance_type, self.supplies)

        pos, supply = self.__check_supply(sustenance_type)
        if player.stamina + supply.energy > 100:
            player.stamina = 100

        player.stamina += supply.energy
        del self.supplies[pos]
        return f"{player.name} sustained successfully with {supply.name}"

    def duel(self, player_name1: str, player_name2: str):
        ...
    
    def next_day(self):
        ...

    def __str__(self):
        ...
