from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def make_sound(self):
        pass

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {type(self).__name__}"

import unittest

from project.animal import Animal
from project.cat import Cat
from project.dog import Dog
from project.kitten import Kitten
from project.tomcat import Tomcat


class Tests(unittest.TestCase):


    def test_kitten_init(self):
        k = Kitten("Meowy", 1)
        # self.assertEqual(k.name, "Meowy")
        # self.assertEqual(k.age, 1)
        # self.assertEqual(k.gender, "Female")
        # self.assertTrue(issubclass(k.__class__, Animal))
        self.assertTrue(issubclass(k.__class__, Cat))


    def test_tomcat_init(self):
        t = Tomcat("Meowy", 15)
        # self.assertEqual(t.name, "Meowy")
        # self.assertEqual(t.age, 15)
        # self.assertEqual(t.gender, "Male")
        # self.assertTrue(issubclass(t.__class__, Animal))
        self.assertTrue(issubclass(t.__class__, Cat))



if __name__ == "__main__":
    unittest.main()




