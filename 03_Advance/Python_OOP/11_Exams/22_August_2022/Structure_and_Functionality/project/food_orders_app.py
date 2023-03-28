from project.client import Client
from project.meals.meal import Meal
from project.validator.validator import Validator


class FoodOrdersApp:

    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.receipt_id = 1

    def __menu_meals(self):
        return {meal.name: meal for meal in self.menu}

    def __client_or_register_new_client(self, phone):
        for client in self.clients_list:
            if client.phone_number == phone:
                return client
        new_client = Client(phone)
        self.clients_list.append(new_client)
        return new_client

    def register_client(self, client_phone_number: str):
        Validator.check_client_phone_number(client_phone_number, self.clients_list)
        self.clients_list.append(Client(client_phone_number))
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        [self.menu.append(meal) for meal in meals if meal.__class__.__name__ in ("Starter", "MainDish", "Dessert")]

    def show_menu(self):
        Validator.check_menu_length(self.menu)
        return "\n".join(str(meal.details()) for meal in self.menu)


    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        Validator.check_menu_length(self.menu)
        client = self.__client_or_register_new_client(client_phone_number)
        all_meals = self.__menu_meals()
        Validator.check_meal_in_menus(meal_names_and_quantities, all_meals)
        Validator.check_quantity(meal_names_and_quantities, all_meals)

        for key, value in meal_names_and_quantities.items():
            all_meals[key].quantity -= value
            client.shopping_cart.append(all_meals[key])

        client.bill += sum(all_meals[key].price * value for key, value in meal_names_and_quantities.items())
        client.ordered_meals.update(meal_names_and_quantities)

        return f"Client {client_phone_number} successfully ordered {', '.join(client.ordered_meals)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.__client_or_register_new_client(client_phone_number)
        Validator.check_client_orders(client.shopping_cart)

        meals = self.__menu_meals()
        for key, value in client.ordered_meals.items():
            meals[key].quantity += value

        client.shopping_cart = []
        client.bill = 0.0
        client.ordered_meals = {}

        return f"Client {client_phone_number} successfully cancelled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__client_or_register_new_client(client_phone_number)
        Validator.check_client_orders(client.shopping_cart)
        total_money = client.bill

        client.shopping_cart = []
        client.bill = 0.0
        client.ordered_meals = {}
        id = self.receipt_id

        self.receipt_id += 1

        return f"Receipt #{id} with total amount of {total_money:.2f} was successfully paid for {client_phone_number}."


    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."





