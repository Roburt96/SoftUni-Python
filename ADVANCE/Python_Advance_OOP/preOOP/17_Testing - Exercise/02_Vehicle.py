from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVenicle(TestCase):

    def setUp(self) -> None:
        self.name = Vehicle(10.0, 150.0)

    def test_class_init(self):
        self.assertEqual(10.0, self.name.fuel)
        self.assertEqual(10.0, self.name.fuel)
        self.assertEqual(150.0, self.name.horse_power)
        self.assertEqual(1.25, self.name.fuel_consumption)

    def test_drive_not_enough_fuel(self):
        with self.assertRaises(Exception) as error:
            self.name.drive(800)
        self.assertEqual("Not enough fuel", str(error.exception))

    def test_drive_enough_fuel(self):
        self.name.drive(5)
        self.assertEqual(3.75, self.name.fuel)

    def test_refuel_if_is_too_much(self):
        with self.assertRaises(Exception) as error:
            self.name.refuel(100)
        self.assertEqual('Too much fuel', str(error.exception))

    def test_refuel_is_lower_or_equal_to_capacity(self):
        self.name.drive(1)
        self.name.refuel(1)
        self.assertEqual(9.75, self.name.fuel)

    def test_str(self):
        result = f"The vehicle has {self.name.horse_power} " \
                 f"horse power with {self.name.fuel} fuel left and {self.name.fuel_consumption} fuel consumption"
        self.assertEqual(result, self.name.__str__())


if __name__ == '__main__':
    main()

# from typing import ClassVar
#
#
# class Vehicle:
#     DEFAULT_FUEL_CONSUMPTION: ClassVar[float] = 1.25
#     fuel_consumption: float
#     fuel: float
#     capacity: float
#     horse_power: float
#
#     def __init__(self, fuel: float, horse_power: float):
#         self.fuel = fuel
#         self.capacity = self.fuel
#         self.horse_power = horse_power
#         self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
#
#     def drive(self, kilometers):
#         fuel_needed = self.fuel_consumption * kilometers
#         if self.fuel < fuel_needed:
#             raise Exception("Not enough fuel")
#         self.fuel -= fuel_needed
#
#     def refuel(self, fuel):
#         if self.fuel + fuel > self.capacity:
#             raise Exception("Too much fuel")
#         self.fuel += fuel
#
#     def __str__(self):
#         return f"The vehicle has {self.horse_power} " \
#                f"horse power with {self.fuel} fuel left and {self.fuel_consumption} fuel consumption"
