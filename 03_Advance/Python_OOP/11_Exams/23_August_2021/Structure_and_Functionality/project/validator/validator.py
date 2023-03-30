class Validator:

    @staticmethod
    def check_name_is_empty_string(name):
        if name == '' or name.isspace():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")