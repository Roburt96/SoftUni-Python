import unittest

from project.booths.open_booth import OpenBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.stolen import Stolen
from project.validator.validator import Validator


# class MyTestCase(unittest.TestCase):
#
#     def setUp(self) -> None:
#         self.stolen = Stolen('Stolen', 1, 1)
#
#     def test_valid_name(self):
#         self.stolen.name = " "
#         Validator.delicacy_check_valid_name(self.stolen.name)
#
#
# if __name__ == '__main__':
#     unittest.main()

openbooth = OpenBooth(1, 10)
openbooth2 = OpenBooth(2, 10)
openbooth.reserve(2)
print(openbooth.price_for_reservation)
print(openbooth.is_reserved)
print(openbooth2.is_reserved)



