class Validator:

    @staticmethod
    def check_empty_string(name: str):
        if name == "" or name.isspace():
            raise ValueError("Name cannot be empty string or white space!")

    @staticmethod
    def check_valid_price(price: float):
        if price <= 0:
            raise ValueError("Price cannot be less than or equal to zero!")

    @staticmethod
    def check_portion_size(portion: float):
        if portion <= 0:
            raise ValueError("Portion cannot be less than or equal to zero!")

    @staticmethod
    def check_brand(brand: str):
        if brand == "" or brand.isspace():
            raise ValueError("Brand cannot be empty string or white space!")

    @staticmethod
    def check_capacity(capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity has to be greater than 0!")

    @staticmethod
    def table_number(number: int, min_people: int, max_people: int, table: str):
        if not min_people <= number <= max_people:
            raise ValueError(f"{table} table's number must be between {min_people} and {max_people} inclusive!")

    @staticmethod
    def check_exist_food(food_name: str, food_list: list, message):
        if any(food_name == food.name for food in food_list):
            raise Exception(message)

    @staticmethod
    def check_exist_drink(drink_name: str, drink_list: list, message):
        if any(drink_name == drink.name for drink in drink_list):
            raise Exception(message)

    @staticmethod
    def check_table_exist(table_number: int, table_list: list, message):
        if any(table_number == table.table_number for table in table_list):
            raise Exception(message)













