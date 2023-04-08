from project.services.base_service import BaseService


class MainService(BaseService):
    __CAPACITY = 30

    def __init__(self, name):
        super().__init__(name, MainService.__CAPACITY)

    def details(self):
        result = f"{self.name} Main Service:\n" \
                 f"Robots: "
        if self.robots:
            result += " ".join([robot.name for robot in self.robots])
        else:
            result += "none"
        return result
