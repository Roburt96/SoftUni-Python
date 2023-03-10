class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = float(fuel)
        self.horse_power = int(horse_power)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        if kilometers * self.fuel_consumption <= self.fuel:
            self.fuel -= kilometers * self.fuel_consumption
vehicle = Vehicle(50, 150)

print(vehicle.fuel)

print(vehicle.horse_power)

print(vehicle.fuel_consumption)