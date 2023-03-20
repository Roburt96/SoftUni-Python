class ChristmasPastryShopApp:

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        ...

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        ...

    def reserve_booth(self, number_of_people: int):
        ...

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        ...

    def leave_booth(self, booth_number: int):
        ...

    def get_income(self):
        ...