from project.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):

    def drive(self, km: int):
        total = km * Motorcycle.DEFAULT_FUEL_CONSUMPTION
        if self.fuel >= total:
            self.fuel -= total