class Validator:

    @staticmethod
    def delicacy_check_valid_name(value):
        if value.isspace() or value == "":
            raise ValueError('Name cannot be null or whitespace!')

    @staticmethod
    def delicacy_check_price_is_less_or_equal_zero(value):
        if value <= 0:
            raise ValueError('Price cannot be less or equal to zero!')

    @staticmethod
    def booth_check_capacity_is_valid_number(value):
        if value < 0:
            raise ValueError('Capacity cannot be a negative number!')

    @staticmethod
    def app_delicacy_check_name_exists(name, delicacies_list):
        if any(name == item.name for item in delicacies_list):
            raise Exception(f'{name} already exists!')

    @staticmethod
    def app_delicacy_valid_type_name(type_delicacy):
        if type_delicacy != 'Stolen' and type_delicacy != 'Gingerbread':
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

    @staticmethod
    def app_booth_check_is_valid_type(type_booth):
        if type_booth != 'Open Booth' and type_booth != 'Private Booth':
            raise Exception(f"{type_booth} is not a valid booth!")

    @staticmethod
    def app_booth_number_exist(booth_number, booth_list):
        if any(booth_number == item.booth_number for item in booth_list):
            raise Exception(f'Booth number {booth_number} already exists!')

    @staticmethod
    def app_check_capacity_on_booth(booth, message):
        if not booth:
            raise Exception(message)

    @staticmethod
    def app_check_booth_number_is_exist(booth_number, message):
        if not booth_number:
            raise Exception(message)

    @staticmethod
    def app_check_delicacy_is_exist(delicacy_name, message):
        if not delicacy_name:
            raise Exception(message)
