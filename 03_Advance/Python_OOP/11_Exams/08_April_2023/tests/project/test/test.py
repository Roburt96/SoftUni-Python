from project.tennis_player import TennisPlayer
from unittest import TestCase

class TestTennisPlayer(TestCase):
    def setUp(self):
        self.player = TennisPlayer('Roburt', 25, 0.0)
        self.second_player = TennisPlayer('Bob', 18, 0.0)

    def test_init_player(self):
        self.assertEqual(self.player.name, 'Roburt')
        self.assertEqual(self.player.age, 25)
        self.assertEqual(self.player.points, 0.0)
        self.assertEqual(self.player.wins, [])

    def test_init_second_player(self):
        self.assertEqual(self.second_player.name, 'Bob')
        self.assertEqual(self.second_player.age, 18)
        self.assertEqual(self.second_player.points, 0.0)
        self.assertEqual(self.second_player.wins, [])

    def test_property_name(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = 'Ra'
        self.assertEqual(str(ve.exception), 'Name should be more than 2 symbols!')

    def test_property_age(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 16
        self.assertEqual(str(ve.exception), 'Players must be at least 18 years of age!')

    def test_successfully_add_win(self):
        self.player.add_new_win('Tennis')
        self.assertEqual(self.player.wins, ['Tennis'])

    def test_unsuccessfully_add_win(self):
        self.player.wins = ['Hockey']
        result = self.player.add_new_win('Hockey')
        self.assertEqual(result , 'Hockey has been already added to the list of wins!')

    def test_lt_method_second_player(self):
        self.second_player.points = 20
        self.player.points = 10
        result = self.player.__lt__(self.second_player)
        self.assertTrue(self.player < self.second_player)
        self.assertEqual(result, 'Bob is a top seeded player and he/she is better than Roburt')

    def test_lt_method_main_player(self):
        self.second_player.points = 10
        self.player.points = 20
        result = self.player.__lt__(self.second_player)
        self.assertEqual(result, 'Roburt is a better player than Bob')

    def test_str(self):
        self.player.add_new_win('Tennis')
        self.player.add_new_win('Hockey')
        self.player.points = 10
        result = str(self.player)
        self.assertEqual(result, f"Tennis Player: Roburt\n"
                                 f"Age: 25\n"
                                 f"Points: 10.0\n"
                                 f"Tournaments won: Tennis, Hockey" )





