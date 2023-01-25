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


    # class Car:
    #     def __init__(self, make, model, fuel_consumption, fuel_capacity):
    #         self.make = make
    #         self.model = model
    #         self.fuel_consumption = fuel_consumption
    #         self.fuel_capacity = fuel_capacity
    #         self.fuel_amount = 0
    #
    #     @property
    #     def make(self):
    #         return self.__make
    #
    #     @make.setter
    #     def make(self, new_value):
    #         if not new_value:
    #             raise Exception("Make cannot be null or empty!")
    #         self.__make = new_value
    #
    #     @property
    #     def model(self):
    #         return self.__model
    #
    #     @model.setter
    #     def model(self, new_value):
    #         if not new_value:
    #             raise Exception("Model cannot be null or empty!")
    #         self.__model = new_value
    #
    #     @property
    #     def fuel_consumption(self):
    #         return self.__fuel_consumption
    #
    #     @fuel_consumption.setter
    #     def fuel_consumption(self, new_value):
    #         if new_value <= 0:
    #             raise Exception("Fuel consumption cannot be zero or negative!")
    #         self.__fuel_consumption = new_value
    #
    #     @property
    #     def fuel_capacity(self):
    #         return self.__fuel_capacity
    #
    #     @fuel_capacity.setter
    #     def fuel_capacity(self, new_value):
    #         if new_value <= 0:
    #             raise Exception("Fuel capacity cannot be zero or negative!")
    #         self.__fuel_capacity = new_value
    #
    #     @property
    #     def fuel_amount(self):
    #         return self.__fuel_amount
    #
    #     @fuel_amount.setter
    #     def fuel_amount(self, new_value):
    #         if new_value < 0:
    #             raise Exception("Fuel amount cannot be negative!")
    #         self.__fuel_amount = new_value
    #
    #     def refuel(self, fuel):
    #         if fuel <= 0:
    #             raise Exception("Fuel amount cannot be zero or negative!")
    #         self.__fuel_amount += fuel
    #         if self.__fuel_amount > self.__fuel_capacity:
    #             self.__fuel_amount = self.__fuel_capacity
    #
    #     def drive(self, distance):
    #         needed = (distance / 100) * self.__fuel_consumption
    #
    #         if needed > self.__fuel_amount:
    #             raise Exception("You don't have enough fuel to drive!")
    #
    #         self.__fuel_amount -= needed