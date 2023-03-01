from project.vehicle import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    def drive(self, km: int):
        total = km * Car.DEFAULT_FUEL_CONSUMPTION
        if self.fuel >= total:
            self.fuel -= total