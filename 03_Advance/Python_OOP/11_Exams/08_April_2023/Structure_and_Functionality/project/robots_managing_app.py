from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService
from project.validator.validator import Validator


class RobotsManagingApp:

    def __init__(self):
        self.robots = []
        self.services = []

    @property
    def __valid_service_type(self):
        return {"MainService": MainService,
                "SecondaryService": SecondaryService}

    @property
    def __valid_robot_type(self):
        return {"MaleRobot": MaleRobot,
                "FemaleRobot": FemaleRobot}

    def __find_robot(self, robot_name: str):
        for robot in self.robots:
            if robot.name == robot_name:
                return robot

    def __find_service(self, service_name):
        for service in self.services:
            if service.name == service_name:
                return service

    def add_service(self, service_type: str, name: str):
        if service_type not in self.__valid_service_type:
            raise Exception("Invalid service type!")
        service = self.__valid_service_type[service_type](name)
        self.services.append(service)
        return f"{service_type} is successfully added."


    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.__valid_robot_type:
            raise Exception("Invalid robot type!")
        robot = self.__valid_robot_type[robot_type](name, kind, price)
        self.robots.append(robot)
        return f"{robot_type} is successfully added."


    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = next((r for r in self.robots if r.name == robot_name), None)
        service = next((s for s in self.services if s.name == service_name), None)

        if robot.__class__.__name__ == "FemaleRobot" and service.__class__.__name__ != "SecondaryService":
            return "Unsuitable service."

        elif robot.__class__.__name__ == "MaleRobot" and service.__class__.__name__ != "MainService":
            return "Unsuitable service."

        Validator.check_capacity(service.capacity, service.robots)
        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.__find_service(service_name)
        robot = next((r for r in service.robots if r.name == robot_name), None)

        if not robot:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."


    def feed_all_robots_from_service(self, service_name: str):
        service = self.__find_service(service_name)
        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self.__find_service(service_name)
        total_sum = sum([r.price for r in service.robots])
        return f"The value of service {service_name} is {total_sum:.2f}."

    def __str__(self):
        result = []
        for s in self.services:
            result.append(s.details())

        return "\n".join(result)




