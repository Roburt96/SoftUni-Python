class Validator:

    @staticmethod
    def valid_phone_number(number):
        if not number.startswith("0") or len(number) != 10 or not number.isdigit():
            raise ValueError("Invalid phone number!")

    @staticmethod
    def valid_meal_name(name):
        if name == "":
            raise ValueError("Name cannot be an empty string!")

    @staticmethod
    def valid_meal_price(price):
        if price <= 0:
            raise ValueError("Invalid price!")

    @staticmethod
    def check_client_phone_number(number, clients_list):
        if any(number == client.phone_number for client in clients_list):
            raise ValueError("The client has already been registered!")

    @staticmethod
    def check_menu_length(menu_list):
        if len(menu_list) < 5:
            raise Exception("The menu is not ready!")

    @staticmethod
    def check_meal_in_menus(meal, all_meals):
        for key in meal:
            if key not in all_meals:
                raise Exception(f"{key} is not in the menu!")

    @staticmethod
    def check_quantity(meal, all_meals):
        for key, quantity in meal.items():
            if quantity > all_meals[key].quantity:
                raise Exception(f"Not enough quantity of {all_meals[key].__class__.__name__}: {key}!")

    @staticmethod
    def check_client_orders(orders):
        if not orders:
            raise Exception("There are no ordered meals!")
