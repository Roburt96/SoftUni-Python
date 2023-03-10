from unittest import TestCase, main

from test.project.train.train import Train


class TestTrain(TestCase):

    def setUp(self) -> None:
        self.my_train = Train('Roburt', 2)

    def test_successfully_initialized(self):
        self.assertEqual('Roburt', self.my_train.name)
        self.assertEqual(2, self.my_train.capacity)
        self.assertEqual([], self.my_train.passengers)
        self.assertEqual("Train is full", self.my_train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", self.my_train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", self.my_train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", self.my_train.PASSENGER_ADD)
        self.assertEqual("Removed {}", self.my_train.PASSENGER_REMOVED)
        self.assertEqual(0, self.my_train.ZERO_CAPACITY)

    def test_capacity_equal_to_passengers(self):
        message = 'Train is full'
        self.my_train.add('uspeshno')
        self.my_train.add('neuspeshno')
        with self.assertRaises(ValueError) as ve:
            self.my_train.add('Tamer')
        self.assertEqual(message, str(ve.exception))
        self.assertEqual(2, len(self.my_train.passengers))

    def test_check_name_already_exists(self):
        self.my_train.capacity = 4
        self.my_train.add('ivan')
        self.my_train.add('gosho')
        with self.assertRaises(ValueError) as ve:
            self.my_train.add('ivan')
        self.assertEqual("Passenger ivan Exists", str(ve.exception))
        self.assertEqual(["ivan", 'gosho'], self.my_train.passengers)

    def test_successfully_add_passenger(self):
        self.my_train.add('Robkata')
        expected = self.my_train.add('tamer')

        self.assertEqual("Added passenger tamer", expected)
        self.assertEqual(['Robkata', 'tamer'], self.my_train.passengers)

    def test_unsuccessfully_remove_passenger(self):
        self.my_train.add('Robkata')

        with self.assertRaises(ValueError) as ve:
            self.my_train.remove('gosho')
        self.assertEqual("Passenger Not Found", str(ve.exception))
        self.assertEqual(['Robkata'], self.my_train.passengers)

    def test_successfully_remove_passenger(self):
        self.my_train.add('Robkata')
        self.my_train.add('Ivan')
        result_removed = self.my_train.remove('Ivan')

        self.assertEqual("Removed Ivan", result_removed)
        self.assertEqual(["Robkata"], self.my_train.passengers)



if __name__ == '__main__':
    main()
