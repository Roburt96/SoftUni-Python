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