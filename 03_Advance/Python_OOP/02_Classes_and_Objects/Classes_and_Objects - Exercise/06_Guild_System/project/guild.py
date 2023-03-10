from project.player import Player


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        else:
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        if player_name not in (x.name for x in self.players):
            return f"Player {player_name} is not in the guild."

        self.players.remove(player_name)
        player_name.guild = "Unaffiliated"
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        result += '\n'.join(hero.player_info() for hero in self.players)
        return result

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())