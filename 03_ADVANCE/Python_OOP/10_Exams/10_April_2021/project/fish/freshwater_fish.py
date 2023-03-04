from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):

    def __init__(self, name, species, price):
        super().__init__(name, species, self.__increase_size, price)

    @property
    def __start_size(self):
        return 3

    @property
    def __increase_size(self):
        return 3

    def eat(self):
        self.size += self.__start_size