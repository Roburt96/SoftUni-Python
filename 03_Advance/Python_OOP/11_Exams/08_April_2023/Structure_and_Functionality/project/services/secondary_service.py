from project.services.base_service import BaseService


class SecondaryService(BaseService):
    __CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, SecondaryService.__CAPACITY)

    def details(self):
        result = f"{self.name} Secondary Service:\n" \
                 f"Robots: "
        if self.robots:
            result += " ".join([robot.name for robot in self.robots])
        else:
            result += "none"
        return result
