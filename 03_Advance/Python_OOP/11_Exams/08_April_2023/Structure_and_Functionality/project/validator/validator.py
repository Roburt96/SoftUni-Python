class Validator:

    @staticmethod
    def valid_name(name: str, message: str):
        if name == '' or name.isspace():
            raise ValueError(message)

    @staticmethod
    def valid_kind(kind: str):
        if kind == '' or kind.isspace():
            raise ValueError("Robot kind cannot be empty!")

    @staticmethod
    def valid_price(price):
        if price <= 0.0:
            raise ValueError("Robot price cannot be less than or equal to 0.0!")

    @staticmethod
    def valid_capacity(capacity):
        if capacity <= 0:
            raise ValueError("Service capacity cannot be less than or equal to 0!")

    @staticmethod
    def check_capacity(capacity, robot_list):
        if capacity == len(robot_list):
            raise ValueError("Not enough capacity for this robot!")

    @staticmethod
    def check_robot_in_service(robot_name, service_list):
        if all(robot != robot_name in robot.name for robot in service_list):
            raise Exception("No such robot in this service!")
