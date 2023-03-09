from project.team import Team
from unittest import TestCase, main

class TestTeam(TestCase):

    def setUp(self):
        self.team = Team('Bears')


    def test_successfully_init(self):
        self.assertEqual(self.team.name, 'Bears')
        self.assertEqual(self.team.members, {})

    def test_property_bad_name(self):
        message = "Team Name can contain only letters!"
        with self.assertRaises(ValueError) as ve:
            self.team.name = 'yes bears'
        self.assertEqual(message, str(ve.exception))

    def test_add_successfully_members(self):
        self.team.add_member(Roburt=18)
        result = self.team.add_member(Ivan=20, Tamer=18, Roburt=18)

        self.assertEqual({'Ivan': 20, "Roburt": 18, "Tamer": 18}, self.team.members)
        self.assertEqual("Successfully added: Ivan, Tamer", result)

    def test_remove_successfully_if_name_in_members(self):
        self.team.add_member(Roburt=18)
        remove = self.team.remove_member("Roburt")

        self.assertEqual({}, self.team.members)
        self.assertEqual("Member Roburt removed", remove)

    def test_remove_successfully_if_name_not_in_members(self):
        self.team.add_member(Roburt=18)
        cant_remove = self.team.remove_member("Ivan")
        self.assertEqual({'Roburt': 18}, self.team.members)

        self.assertEqual({'Roburt': 18}, self.team.members)
        self.assertEqual("Member with name Ivan does not exist", cant_remove)

    def test_other_team_gt_method_main_team(self):

        self.team.add_member(Roburt=20)
        new_team = Team('Cats')
        new_team.add_member(Ivan=20)
        new_team.add_member(Tamer=18)
        len_result =  (len(self.team.members) <= len(new_team.members))
        result = False

        self.assertEqual(result, False)
        self.assertTrue(len_result)

    def test_main_team_gt_other_team(self):
        new_team = Team("Cats")
        new_team.add_member(Petar=20)
        self.team.add_member(Roburt=18)
        self.team.add_member(Goshko=18)
        len_result = (len(self.team.members) > len(new_team.members))
        result = True

        self.assertEqual(result, True)
        self.assertTrue(len_result)

    def test_len_members(self):
        self.team.add_member(Roburt=18)
        result = len(self.team.members)

        self.assertEqual(1, result)
        self.assertEqual({'Roburt': 18}, self.team.members)

    def test_add_teams_togethers(self):
        team_two = Team("Cats")
        self.team.add_member(Roburt=18)
        team_two.add_member(Goshko=18, Petar=20)

        result = self.team + team_two

        self.assertEqual(result.name, "BearsCats")
        self.assertEqual(result.members, {'Roburt': 18, 'Goshko': 18, 'Petar': 20})

    def test_successfully_str(self):
        self.team.add_member(Bobi=20, Asen=18, Ceco=16)

        result = "Team name: Bears\n" \
                 "Member: Bobi - 20-years old\n" \
                 "Member: Asen - 18-years old\n" \
                 "Member: Ceco - 16-years old" \

        self.assertEqual(result, self.team.__str__())

if __name__ == "__main__":
    main()


