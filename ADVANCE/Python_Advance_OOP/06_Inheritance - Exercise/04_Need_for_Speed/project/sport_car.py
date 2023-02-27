from project.car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    def drive(self, km: int):
        total = km * SportCar.DEFAULT_FUEL_CONSUMPTION
        if self.fuel >= total:
            self.fuel -= total