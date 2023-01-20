from abc import ABC, abstractmethod
class Venicle(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def drive(self, distance):
        pass
    @abstractmethod
    def refuel(self, fuel):
        pass

class Car(Venicle):
    CAR_CONSUM_INC = 0.9
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        super().__init__()
        self.fuel_quantity = fuel_quantity  # 20
        self.fuel_consumption = fuel_consumption  # 5 per km


    def drive(self, drive):
        consum = ((self.fuel_consumption + Car.CAR_CONSUM_INC) * drive)
        if consum <= self.fuel_quantity:
            self.fuel_quantity -= consum
    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Venicle):
    TRUCK_CONSUM_INC = 1.6

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        super().__init__()
        self.fuel_quantity = fuel_quantity  # 20
        self.fuel_consumption = fuel_consumption   # 5 per km

    def drive(self, drive):
        consum = ((self.fuel_consumption + Truck.TRUCK_CONSUM_INC) * drive)
        if consum <= self.fuel_quantity:
            self.fuel_quantity -= consum


    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)