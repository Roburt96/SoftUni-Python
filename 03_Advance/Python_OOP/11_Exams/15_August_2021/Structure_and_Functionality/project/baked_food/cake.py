from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):
    def __init__(self, name: str, price: float):
        super().__init__(name, 245, price)

    def __repr__(self):
        return f"{super().__repr__()}"