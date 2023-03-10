from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    
    def __init__(self, name):
        super().__init__(name, self.__aqua_capacity)
    
    @property
    def __aqua_capacity(self):
        return 25