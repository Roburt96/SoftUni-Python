from project.elf import Elf


class MuseElf(Elf):

    def __init__(self, username, level):
        super().__init__(username, level)

    def __str__(self):
        return f"{self.username} of type {MuseElf.__name__} has level {self.level}"

