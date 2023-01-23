from unittest import TestCase, main


class TestCar(TestCase):

    def setUp(self) -> None:
        self.name = Car("Jeep", 'Wrangler', 10, 60)

    def test_succsessfuly_initialisation(self):
        self.assertEqual("Jeep", self.name.make)
        self.assertEqual('Wrangler', self.name.model)
        self.assertEqual(10, self.name.fuel_consumption)
        self.assertEqual(60, self.name.fuel_capacity)
        self.assertEqual(0, self.name.fuel_amount)

    def test_make_throw_value(self):
        with self.assertRaises(Exception) as error:
            self.name.make = ''
        self.assertEqual("Make cannot be null or empty!", str(error.exception))

    def test_model_thow_value(self):
        with self.assertRaises(Exception) as error:
            self.name.model = ''
        self.assertEqual("Model cannot be null or empty!", str(error.exception))

    def test_fuel_consumption_check_zero_or_negative(self):
        with self.assertRaises(Exception) as error:
            self.name.fuel_consumption  = -2
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(error.exception))

    def test_fuel_capacity_check_zero_or_negative(self):
        with self.assertRaises(Exception) as error:
            self.name.fuel_capacity = -3
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(error.exception))

    def test_fuel_amount_check_negative(self):
        with self.assertRaises(Exception) as error:
            self.name.fuel_amount = -10
        self.assertEqual("Fuel amount cannot be negative!", str(error.exception))

    def test_check_refuel_is_zero_or_negative(self):
        with self.assertRaises(Exception) as error:
            self.name.refuel(-10)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(error.exception))

    def test_check_added_fuel_with_fuel_capacity(self):
        self.name.refuel(70)
        self.assertEqual(60, self.name.fuel_amount)

        self.name.fuel_amount = 0
        self.name.refuel(20)
        self.assertEqual(20, self.name.fuel_amount)

    def test_not_enough_fuel_to_cover_the_distance(self):
        with self.assertRaises(Exception) as error:
            self.name.fuel_amount = 5
            self.name.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(error.exception))

    def test_fuel_amount_cannot_be_zero_or_negative(self):
        self.name.fuel_amount = 50
        self.name.drive(10)
        self.assertEqual(49, self.name.fuel_amount)


if __name__ == '__main__':
    main()