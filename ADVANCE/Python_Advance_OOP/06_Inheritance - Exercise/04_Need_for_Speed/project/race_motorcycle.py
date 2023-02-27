from project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

    def drive(self, km: int):
        total = km * RaceMotorcycle.DEFAULT_FUEL_CONSUMPTION
        if self.fuel >= total:
            self.fuel -= total