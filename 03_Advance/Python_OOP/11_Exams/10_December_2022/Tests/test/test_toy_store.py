from project.toy_store import ToyStore
from unittest import TestCase

class TestToyStore(TestCase):

    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_init(self):
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_unsuccessfully_add_toy_raise_exception(self):
        self.toy_store.toy_shelf = {
            "A": 'None',
        }
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("B", "NewToy")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_toy_already_added_to_the_shelf(self):
        self.toy_store.toy_shelf = {
            "A": "Roburt",
        }
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Roburt")
        self.assertEqual(str(ex.exception), "Toy is already in shelf!")

    def test_shelf_not_equal_to_none(self):
        self.toy_store.add_toy("A", "Taken")

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "NotTaken")

        self.assertEqual(str(ex.exception), "Shelf is already taken!")
        self.assertTrue(self.toy_store.toy_shelf["A"] is not None)

    def test_successfully_add_toy(self):
        self.toy_store.toy_shelf = {
            "A": None,
        }
        result = self.toy_store.add_toy("A", "AddToy")
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": "AddToy",
        })
        self.assertEqual(result, "Toy:AddToy placed successfully!")

    def test_try_to_remove_toy_not_exist(self):
        self.toy_store.toy_shelf = {
            "A": "ToyHere",
        }
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("B", "RemoveToy")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_try_to_remove_toy_from_shelf_with_diff_name(self):
        self.toy_store.toy_shelf = {
            "A": "RemoveToy",
        }
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "CantRemove")
        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")

    def test_successfully_remove_toy(self):
        self.toy_store.toy_shelf = {
            "A": "RemoveToy",
        }
        result = self.toy_store.remove_toy("A", "RemoveToy")
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": None,
        })
        self.assertEqual(result, "Remove toy:RemoveToy successfully!")
