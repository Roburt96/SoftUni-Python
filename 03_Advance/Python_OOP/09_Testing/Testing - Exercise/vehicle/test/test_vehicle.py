from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.my_car = Vehicle(10.0, 100.0)

    def test_class_successfully_init(self):
        self.assertEqual(self.my_car.fuel, 10.0)
        self.assertEqual(self.my_car.horse_power, 100.0)
        self.assertEqual(self.my_car.capacity, 10.0)
        self.assertEqual(self.my_car.fuel_consumption, 1.25)

    def test_cant_drive_kilometers_not_enough_fuel(self):
        with self.assertRaises(Exception) as error:
            self.my_car.drive(800)
        self.assertEqual("Not enough fuel", str(error.exception))

    def test_can_drive_kilometers(self):
        self.my_car.drive(5)
        self.assertEqual(self.my_car.fuel, 3.75)

    def test_refuel_more_than_capacity(self):
        with self.assertRaises(Exception) as error:
            self.my_car.refuel(1000)
        self.assertEqual("Too much fuel", str(error.exception))

    def test_correct_refuel(self):
        self.my_car.drive(1)
        self.my_car.refuel(1)
        self.assertEqual(9.75, self.my_car.capacity)

    def test_str_method(self):
        result = f"The vehicle has {self.my_car.horse_power} " \
                 f"horse power with {self.my_car.fuel} fuel left and {self.my_car.fuel_consumption} fuel consumption"
        self.assertEqual(result, self.my_car.__str__())

