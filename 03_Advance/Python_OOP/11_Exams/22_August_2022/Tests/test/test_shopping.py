

from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class ShoppingCartTests(TestCase):

    def setUp(self) -> None:
        self.shopping_cart_1 = ShoppingCart('Elimex', 1000)
        self.shopping_cart_2 = ShoppingCart('VikiVat', 1000)
    def test_correct_init(self):
        self.assertEqual(self.shopping_cart_1.shop_name, 'Elimex')
        self.assertEqual(self.shopping_cart_1.budget, 1000)
        self.assertEqual(self.shopping_cart_1.products, {})

    def test_shop_name_no_upper_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart_1.shop_name = 'elimex'

        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_add_to_cart_expensive_product_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart_1.add_to_cart('Switch', 120)

        self.assertEqual(str(ve.exception), "Product Switch cost too much!")

    def test_add_to_cart_successfully(self):
        message = self.shopping_cart_1.add_to_cart('Switch', 20)
        expected_message = f"Switch product was successfully added to the cart!"

        self.assertEqual(message, expected_message)
        self.assertEqual(self.shopping_cart_1.products['Switch'], 20)

    def test_remove_from_cart_invalid_product_name_raise_value_error(self):
        product_name = 'Glue'
        self.shopping_cart_1.products = {'Tools': 20}

        with self.assertRaises(ValueError) as ve:
            self.shopping_cart_1.remove_from_cart(product_name)

        self.assertEqual(str(ve.exception), f"No product with name {product_name} in the cart!")

    def test_successful_remove_from_card(self):
        product_name = "Music DVD"
        product_price = 100
        self.shopping_cart_1.products = {product_name: product_price, "two": 1}
        result = self.shopping_cart_1.remove_from_cart(product_name)
        self.assertEqual(f"Product {product_name} was successfully removed from the cart!", result)
        self.assertEqual(1, len(self.shopping_cart_1.products))

    def test_add_two_instances(self):
        self.shopping_cart_1.products = {'Tools': 20}
        self.shopping_cart_2.products = {'Parts': 30}
        shopping_cart_3 = self.shopping_cart_1.__add__(self.shopping_cart_2)

        expected_name = f"ElimexVikiVat"
        expected_budget = 2000
        expected_products = {'Tools': 20, 'Parts': 30}

        self.assertEqual(shopping_cart_3.shop_name, expected_name)
        self.assertEqual(shopping_cart_3.budget, expected_budget)
        self.assertEqual(shopping_cart_3.products, expected_products)
        self.assertIsInstance(self.shopping_cart_1.__add__(self.shopping_cart_2), type(shopping_cart_3))

    def test_buy_product_insufficient_budget_raise_value_error(self):
        self.shopping_cart_1.products = {'Tools': 600, 'Parts': 500}
        expected_message = f"Not enough money to buy the products! Over budget with 100.00lv!"

        with self.assertRaises(ValueError) as ve:
            self.shopping_cart_1.buy_products()

        self.assertEqual(str(ve.exception), expected_message)


    def test_buy_products_successfully(self):
        self.shopping_cart_1.products = {'Tools': 400, 'Parts': 500}

        message = self.shopping_cart_1.buy_products()
        expected_message = 'Products were successfully bought! Total cost: 900.00lv.'

        self.assertEqual(message, expected_message)


if __name__ == '__main__':
    main()