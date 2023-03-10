from project.car import Car
from project.vehicle import Vehicle


class FamilyCar(Car):

    def drive(self, km: int):
        total = km * Car.DEFAULT_FUEL_CONSUMPTION
        if self.fuel >= total:
            self.fuel -= total
