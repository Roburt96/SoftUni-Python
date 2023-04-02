from project.pet_shop import PetShop
from unittest import TestCase

class TestPetShop(TestCase):

    def setUp(self) -> None:
        self.shop = PetShop('Maverick')

    def test_successfully_init(self):
        self.assertEqual(self.shop.name, 'Maverick')
        self.assertEqual(self.shop.food, {})
        self.assertEqual(self.shop.pets, [])

    def test_add_zero_or_less_food(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.add_food('banana', -1)
        self.assertEqual(str(ve.exception), 'Quantity cannot be equal to or less than 0')


    def test_add_and_increase_food_value(self):
        self.shop.add_food('banana', 2)
        result = self.shop.add_food('apple', 2)
        self.assertEqual(result, "Successfully added 2.00 grams of apple.")
        self.assertEqual(self.shop.food, {'banana': 2, 'apple': 2})

    def test_add_pet_successfully(self):
        result = self.shop.add_pet('Doggo')
        self.shop.add_pet('Bat Qnko')
        self.assertEqual(result, "Successfully added Doggo.")
        self.assertEqual(self.shop.pets, ['Doggo', 'Bat Qnko'])

    def test_unsuccessfully_add_dog_with_same_name(self):
        self.shop.pets = ['Doggo']
        with self.assertRaises(Exception) as err:
            self.shop.add_pet('Doggo')
        self.assertEqual(str(err.exception), "Cannot add a pet with the same name")

    def test_try_feed_pet_not_in_list(self):
        self.shop.add_pet('Doggo')
        with self.assertRaises(Exception) as err:
            self.shop.feed_pet('banana', 'Not a pet')
        self.assertEqual(str(err.exception), "Please insert a valid pet name")

    def test_try_feed_pet_with_food_not_in_list(self):
        self.shop.add_food('banana', 2)
        self.shop.add_pet('Doggo')
        result = self.shop.feed_pet('Not a food', 'Doggo')
        self.assertEqual(result, "You do not have Not a food")

    def test_value_of_food_below_100(self):
        self.shop.add_food('banana', 99)
        self.shop.add_pet('Doggo')
        self.assertEqual(self.shop.feed_pet('banana', 'Doggo'), "Adding food...")
        self.assertEqual(self.shop.food['banana'], 1099.00)

    def test_value_of_food_more_than_100(self):
        self.shop.add_food('banana', 200)
        self.shop.add_pet('monkey')
        result = self.shop.feed_pet('banana', 'monkey')
        self.assertEqual(result, "monkey was successfully fed")
        self.assertEqual(self.shop.food['banana'], 100)

    def test_repr(self):
        self.shop.add_pet('Doggo')
        self.shop.add_pet('Kitty')
        result = "Shop Maverick:\n" \
                 "Pets: Doggo, Kitty"
        self.assertEqual(repr(self.shop), result)