from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def calculate_area(self):
        return pi * self.__radius * self.__radius

    def calculate_perimeter(self):
        return  2 * pi * self.__radius


class Rectangle(Shape):
    def __init__(self, height, width):
        super().__init__()

        self.__height = height
        self.__width = width

    def calculate_area(self):
        return self.__height * self.__width

    def calculate_perimeter(self):
        return 2 * (self.__width + self.__height)

circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())