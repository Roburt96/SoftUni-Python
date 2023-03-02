from abc import ABC


class Vehicle(ABC):

    def drive(self, distance):
        pass

    def refuel(self, fuel):
        pass


class Car(Vehicle):
    SUMMER_FUEL_INCREASE = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        total_fuel_consumption = distance * (self.fuel_consumption + self.SUMMER_FUEL_INCREASE)
        if total_fuel_consumption <= self.fuel_quantity:
            self.fuel_quantity -= total_fuel_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    SUMMER_FUEL_INCREASE = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        total_fuel_consumption = distance * (self.fuel_consumption + self.SUMMER_FUEL_INCREASE)
        if total_fuel_consumption <= self.fuel_quantity:
            self.fuel_quantity -= total_fuel_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)