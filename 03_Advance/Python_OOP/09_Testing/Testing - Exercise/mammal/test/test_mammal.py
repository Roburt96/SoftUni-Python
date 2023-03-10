from unittest import TestCase, main

from mammal.project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.name = Mammal('Roburt', 'lion', 'rawr')

    def test_successfully_init(self):
        self.assertEqual(self.name.name, 'Roburt')
        self.assertEqual(self.name.type, 'lion')
        self.assertEqual(self.name.sound, 'rawr')
        self.assertEqual(self.name.get_kingdom(), "animals")

    def test_sound_of_this_animal(self):
        self.assertEqual('Roburt makes rawr', self.name.make_sound())

    def test_correct_kingdom(self):
        self.assertEqual("animals", self.name.get_kingdom())

    def test_info_about_type_of_animal(self):
        self.assertEqual('Roburt is of type lion', self.name.info())

if __name__ == '__main__':
    main()