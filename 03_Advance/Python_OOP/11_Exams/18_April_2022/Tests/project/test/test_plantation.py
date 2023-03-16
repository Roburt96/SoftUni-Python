from project.plantation import Plantation
from unittest import TestCase, main

class TestPlantation(TestCase):
    def setUp(self):
        self.plantation = Plantation(10)

    def test_successfully_init(self):
        self.assertEqual(self.plantation.size, 10)
        self.assertEqual(self.plantation.plants, {})
        self.assertEqual(self.plantation.workers, [])

    def test_init_with_negative_size(self):
        with self.assertRaises(ValueError) as e:
            Plantation(-1)
        self.assertEqual(str(e.exception), "Size must be positive number!")

    def test_init_with_zero_size(self):
        with self.assertRaises(ValueError) as e:
            Plantation(0)
        self.assertEqual(str(e.exception), "Size must be positive number!")

    def test_unsuccessfully_hire_worker(self):
        self.plantation.workers = ['worker']
        with self.assertRaises(ValueError) as e:
            self.plantation.hire_worker("worker")
        self.assertEqual(str(e.exception), "Worker already hired!")

    def test_successfully_hire_worker(self):
        self.plantation.workers = []
        self.plantation.hire_worker("worker")
        self.assertEqual(self.plantation.workers, ['worker'])

    def test_successfully_show_len_of_plants(self):
        plant = Plantation(1)
        plant.hire_worker("worker1")
        plant.hire_worker("worker2")
        plant.plants["worker1"] = ["flower1"]
        plant.plants["worker2"] = ["flower2"]
        self.assertEqual(len(plant), 2)

    def test_successfully_show_worker_not_in_workers(self):
        self.plantation.workers = ['worker1', 'worker2']
        with self.assertRaises(ValueError) as e:
            self.plantation.planting('worker3', 'flower')
        self.assertEqual(str(e.exception), "Worker with name worker3 is not hired!")

    def test_plantation_is_full(self):
        self.plantation.size = 1
        self.plantation.plants = {'worker1': 'flower'}
        result = (self.plantation.size >= len(self.plantation.plants))
        with self.assertRaises(ValueError) as e:
            self.plantation.planting('worker2', 'flower2')
        self.assertTrue(result, "The plantation is full!")

    def test_successfully_add_plant_to_the_worker(self):
        self.plantation.hire_worker('worker1')
        self.plantation.planting('worker1', 'flower2')
        self.assertEqual("worker1 planted flower2.", self.plantation.planting('worker1', 'flower2'))

    def test_successfully_add_worker_and_plant(self):
        self.plantation.hire_worker('worker1')
        self.plantation.plants = {}
        result = self.plantation.planting('worker1', 'flower1')
        self.assertEqual("worker1 planted it's first flower1.", result)

    def test_show_str_method(self):
        self.assertEqual("Plantation size: 10\n", self.plantation.__str__())
        self.plantation.hire_worker("worker1")
        self.plantation.planting("worker1", "flower1")
        self.assertEqual("Plantation size: 10\n"
                         "worker1\n"
                         "worker1 planted: flower1", self.plantation.__str__())

    def test_repr(self):
        self.plantation.hire_worker("worker1")
        self.plantation.hire_worker("worker2")
        result = "Size: 10\n" \
                 "Workers: worker1, worker2"
        self.assertEqual(result, self.plantation.__repr__())


