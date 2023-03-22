from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen
from project.validator.validator import Validator


class ChristmasPastryShopApp:

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    @property
    def __valid_delicacy(self):
        return {'Stolen': Stolen, 'Gingerbread': Gingerbread}

    @property
    def __valid_booths(self):
        return {'Open Booth': OpenBooth, 'Private Booth': PrivateBooth}

    def __booth_to_reserve(self, number_of_people: int):
        for b in self.booths:
            if not b.is_reserved and b.capacity >= number_of_people:
                return b

    def __get_booth_number(self, number_booth):
        for n in self.booths:
            if number_booth == n.booth_number:
                return n

    def __get_delicacy_name(self, name_delicacy):
        for d in self.delicacies:
            if name_delicacy == d.name:
                return d

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        Validator.app_delicacy_valid_type_name(type_delicacy)
        Validator.app_delicacy_check_name_exists(name, self.delicacies)

        current = self.__valid_delicacy[type_delicacy](name, price)
        self.delicacies.append(current)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        Validator.app_booth_check_is_valid_type(type_booth)
        Validator.app_booth_number_exist(booth_number, self.booths)

        current = self.__valid_booths[type_booth](booth_number, capacity)
        self.booths.append(current)
        return f"Added booth number {booth_number} to the pastry shop."

    def reserve_booth(self, number_of_people: int):
        curr_booth = self.__booth_to_reserve(number_of_people)
        Validator.app_check_capacity_on_booth(curr_booth, f"No available booth for {number_of_people} people!")

        curr_booth.reserve(number_of_people)
        return f"Booth {curr_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        curr_number = self.__get_booth_number(booth_number)
        Validator.app_check_booth_number_is_exist(curr_number, f"Could not find booth {booth_number}!")

        curr_delicacy = self.__get_delicacy_name(delicacy_name)
        Validator.app_check_delicacy_is_exist(curr_delicacy, f"No {delicacy_name} in the pastry shop!")

        curr_number.delicacy_orders.append(curr_delicacy)
        return f"Booth {curr_number.booth_number} ordered {curr_delicacy.name}."

    def leave_booth(self, booth_number: int):
        curr_booth = self.__get_booth_number(booth_number)
        curr_bill = curr_booth.calculate_bill()
        self.income += curr_bill
        curr_booth.leave_booth()

        return f"Booth {curr_booth.booth_number}:\n" \
               f"Bill: {curr_bill:.2f} lv"

    def get_income(self):
        return f"Income: {self.income:.2f}lv"