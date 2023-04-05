
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.validator.validator import Validator


class Bakery:

    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_empty_string(value)
        self.__name = value

    @property
    def __food_type(self):
        return {'Bread': Bread,
                'Cake': Cake}

    @property
    def drink_type(self):
        return {'Tea': Tea,
                'Water': Water}

    @property
    def table_type(self):
        return {'InsideTable': InsideTable,
                'OutsideTable': OutsideTable}

    def __reserve_table(self, number_people: int):
        for t in self.tables_repository:
            if t.capacity >= number_people and not t.is_reserved:
                return t

    def __find_table(self, table_number: int):
        for t in self.tables_repository:
            if t.table_number == table_number:
                return t

    def __find_food(self, food_name):
        for f in self.food_menu:
            if f.name == food_name:
                return f

    def add_food(self, food_type: str, name: str, price: float):
        food = self.__food_type[food_type](name, price)
        Validator.check_exist_food(name, self.food_menu, f"{food_type} {name} is already in the menu!")

        self.food_menu.append(food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand:str):
        drink = self.drink_type[drink_type](name, portion, brand)
        Validator.check_exist_drink(name, self.drinks_menu, f"{drink_type} {name} is already in the menu!")

        self.drinks_menu.append(drink)
        return f"Added {name} ({drink_type}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        table = self.table_type[table_type](table_number, capacity)
        Validator.check_table_exist(table_number, self.tables_repository, f"Table {table_number} is already in the bakery!")

        self.tables_repository.append(table)
        return f"Added table number {table_number} to the bakery"

    def reserve_table(self, number_of_people: int):
        table = self.__reserve_table(number_of_people)
        if table:
            table.is_reserved = True
            table.number_of_people += number_of_people
            return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        table = self.__find_table(table_number)
        if not table:
            return f"Could not find table {table_number}"


        def __get_menu_food():
            menu = {f.name: f for f in self.food_menu}
            return menu


        menu_food = __get_menu_food()
        have_food = [f"Table {table_number} ordered:"]
        not_have_food = [f"{self.name} does not have in the menu:"]
        for f_name in food_names:
            if f_name in menu_food:
                table.order_food(self.__find_food(f_name))
                have_food.append(f"{menu_food[f_name]}")
            else:
                not_have_food.append(str(f_name))
        return '\n'.join(have_food + not_have_food)


    def order_drink(self, table_number: int, *drink_names: tuple):
        table = self.__find_table(table_number)
        if not table:
            return f"Could not find table {table_number}"

        def __get_menu_drinks():
            menu = {f.name: f for f in self.drinks_menu}
            return menu

        menu_drinks = __get_menu_drinks()
        have_drinks = [f"Table {table_number} ordered:"]
        not_have_drinks = [f"{self.name} does not have in the menu:"]

        for d in drink_names:
            if d in menu_drinks:
                table.order_drink(menu_drinks[d])
                have_drinks.append(f"{menu_drinks[d]}")
            else:
                not_have_drinks.append(str(d))
        return '\n'.join(have_drinks + not_have_drinks)

    def leave_table(self, table_number: int):
        table = self.__find_table(table_number)
        table_bill = table.get_bill()
        self.total_income += table_bill
        table.clear()

        return f"Table: {table_number}\nBill: {table_bill:.2f}"

    def get_free_tables_info(self):
        return "\n".join(t.free_table_info() for t in self.tables_repository)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}"







