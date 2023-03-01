from project.vehicle import Vehicle


class Motorcycle(Vehicle):

    def drive(self, km: int):
        if self.fuel >= km * Vehicle.DEFAULT_FUEL_CONSUMPTION:
            self.fuel -= km * Vehicle.DEFAULT_FUEL_CONSUMPTION