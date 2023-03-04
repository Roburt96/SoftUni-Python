
from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.__start_size, price)
    
    @property
    def __start_size(self):
        return 5

    @property
    def __increase_size(self):
        return 2

    def eat(self):
        self.size = self.__increase_size

