from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self) -> None:
        self.name = Mammal('Pumba', 'pig', 'oink')

    def test_succsesfly_initialisation(self):
        self.assertEqual('Pumba', self.name.name)
        self.assertEqual('pig', self.name.type)
        self.assertEqual('oink', self.name.sound)
        self.assertEqual('animals', self.name.get_kingdom())

    def test_what_sound_making(self):
        self.assertEqual('Pumba makes oink', self.name.make_sound())

    def test_get_the_correct_kingdom(self):
        self.assertEqual('animals', self.name.get_kingdom())

    def test_get_more_information_about_type(self):
        self.assertEqual('Pumba is of type pig', self.name.info())

if __name__ == '__main__':
    main()

#
# class Mammal:
#     def __init__(self, name, mammal_type, sound):
#         self.name = name
#         self.type = mammal_type
#         self.sound = sound
#         self.__kingdom = "animals"
#
#     def make_sound(self):
#         return f"{self.name} makes {self.sound}"
#
#     def get_kingdom(self):
#         return self.__kingdom
#
#     def info(self):
#         return f"{self.name} is of type {self.type}"