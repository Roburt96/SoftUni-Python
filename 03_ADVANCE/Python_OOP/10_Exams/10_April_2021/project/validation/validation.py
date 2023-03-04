class Validator:


    @staticmethod
    def check_for_empty_string(name, error_message):
        if name == "":
            raise ValueError(error_message)

    @staticmethod
    def check_price_equal_or_below_zero(value, error_message):
        if value <= 0:
            raise ValueError(error_message)
