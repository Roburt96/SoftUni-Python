from unittest import TestCase, main
from project.hero import Hero
class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero('Roburt', 1, 100, 50)
        self.enemy_hero = Hero("Tamer", 1, 50, 5)

    def test_class_init(self):
        self.assertEqual('Roburt', self.hero.username)
        self.assertEqual(50, self.hero.level)
        self.assertEqual(100.0, self.hero.health)
        self.assertEqual(10.0, self.hero.damage)

    def test_battle_if_enemy_equal_to_username(self):
        with self.assertRaises(Exception) as error:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(error.exception))

    def test_battle_if_username_have_zero_or_negative_hp(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_if_enemy_have_zero_or_negative_hp(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)
        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest", str(ve.exception))

    def test_if_both_player_have_0_hp_draw(self):
        self.hero.damage = 1000
        self.enemy_hero.damage = 1000
        battle = self.hero.battle(self.enemy_hero)
        self.assertEqual('Draw', battle)

    def test_if_player_defeat_enemy(self):
        self.hero.damage = 1000
        self.hero.health = 10000
        battle = self.hero.battle(self.enemy_hero)
        self.assertEqual('You win', battle)

    def test_if_hero_gains_stats_after_a_win(self):
        self.hero.health = 1000
        self.hero.damage = 1000
        expected_level = self.hero.level + 1
        expected_health = self.hero.health - self.enemy_hero.damage + 5
        expected_damage = self.hero.damage + 5

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_damage, self.hero.damage)
        self.assertEqual("You win", result)

    def test_if_hero_looses_battle_and_enemy_gains_stats(self):
        self.hero.health = 1
        self.hero.damage = 1
        self.enemy_hero.health = 555
        self.enemy_hero.damage = 555
        self.enemy_hero.level = 20
        if_win_lvl = self.enemy_hero.level + 1
        if_win_health = self.enemy_hero.health - self.hero.damage + 5
        if_win_dmg = self.enemy_hero.damage + 5
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(if_win_lvl, self.enemy_hero.level)
        self.assertEqual(if_win_health, self.enemy_hero.health)
        self.assertEqual(if_win_dmg, self.enemy_hero.damage)
        self.assertEqual("You lose", result)

    def test_str_method(self):
        expected = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                   f"Health: {self.hero.health}\n" \
                   f"Damage: {self.hero.damage}\n"
        self.assertEqual(expected, self.hero.__str__())


if __name__ == '__main__':
    main()

# class Hero:
#     username: str
#     health: float
#     damage: float
#     level: int
#
#     def __init__(self, username: str, level: int, health: float, damage: float):
#         self.username = username
#         self.level = level
#         self.health = health
#         self.damage = damage
#
#     def battle(self, enemy_hero):
#         if enemy_hero.username == self.username:
#             raise Exception("You cannot fight yourself")
#
#         if self.health <= 0:
#             raise ValueError("Your health is lower than or equal to 0. You need to rest")
#
#         if enemy_hero.health <= 0:
#             raise ValueError(f"You cannot fight {enemy_hero.username}. He needs to rest")
#
#         player_damage = self.damage * self.level
#         enemy_hero_damage = enemy_hero.damage * enemy_hero.level
#
#         self.health -= enemy_hero_damage
#         enemy_hero.health -= player_damage
#
#         if self.health <= 0 and enemy_hero.health <= 0:
#             return "Draw"
#
#         if enemy_hero.health <= 0:
#             self.level += 1
#             self.health += 5
#             self.damage += 5
#             return "You win"
#
#         enemy_hero.level += 1
#         enemy_hero.health += 5
#         enemy_hero.damage += 5
#         return "You lose"
#
#     def __str__(self):
#         return f"Hero {self.username}: {self.level} lvl\n" \
#                f"Health: {self.health}\n" \
#                f"Damage: {self.damage}\n"