from project.drink.drink import Drink


class Water(Drink):
    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, 1.50, brand)

    def __repr__(self):
        return f"{super().__repr__()}"