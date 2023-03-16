from unittest import TestCase, main
from project.hero import Hero
class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero('Batman', 1, 100, 100)
        self.enemy_hero = Hero('Superman', 1, 50, 50)

    def test_successfully_init(self):
        self.assertEqual(self.hero.username, 'Batman')
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.health, 100.0)
        self.assertEqual(self.hero.damage, 100)

    def test_battle_with_enemy_with_same_name(self):
        with self.assertRaises(Exception) as error:
            self.hero.battle(self.hero)
        self.assertEqual(str(error.exception), "You cannot fight yourself")

    def test_hero_health_equal_or_less_than_0(self):
        self.hero.health = -2
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)
        self.assertEqual(str(ve.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_enemy_hero_health_equal_or_less_than_0(self):
        self.enemy_hero.health = -2
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)
        self.assertEqual(str(ve.exception), f"You cannot fight {self.enemy_hero.username}. He needs to rest")

    def test_fight_and_both_have_same_health(self):
        self.hero.damage = 500
        self.enemy_hero.damage = 500
        battle = self.hero.battle(self.enemy_hero)
        self.assertEqual(battle, 'Draw')

    def test_hero_defeat_enemy(self):
        self.hero.damage = 500
        self.enemy_hero.damage = 1
        battle = self.hero.battle(self.enemy_hero)
        self.assertEqual(battle, "You win")

    def test_hero_gains_stats_after_win(self):
        self.hero.damage = 500
        self.hero.level = 1
        self.enemy_hero.damage = 1
        up_level = self.hero.level + 1
        up_health = self.hero.health - self.enemy_hero.damage + 5
        up_damage = self.hero.damage + 5
        battle = self.hero.battle(self.enemy_hero)
        self.assertEqual(up_level, self.hero.level)
        self.assertEqual(up_health, self.hero.health)
        self.assertEqual(up_damage, self.hero.damage)
        self.assertEqual(battle, 'You win')

    def test_enemy_hero_defeat_hero(self):
        self.hero.damage = 1
        self.enemy_hero.damage = 500
        battle = self.hero.battle(self.enemy_hero)
        self.assertEqual(battle, "You lose")

    def test_enemy_hero_gains_stats_after_win(self):
        self.hero.damage = 1
        self.hero.health = 1
        self.enemy_hero.damage = 500
        self.enemy_hero.health = 500
        self.enemy_hero.level = 20

        up_level = self.enemy_hero.level + 1
        up_health = self.enemy_hero.health - self.hero.damage + 5
        up_damage = self.enemy_hero.damage + 5
        battle = self.hero.battle(self.enemy_hero)
        self.assertEqual(up_level, self.enemy_hero.level)
        self.assertEqual(up_health, self.enemy_hero.health)
        self.assertEqual(up_damage, self.enemy_hero.damage)
        self.assertEqual(battle, 'You lose')

    def test_str_method(self):
        result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"
        self.assertEqual(str(self.hero), result)