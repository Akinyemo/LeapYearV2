import unittest
import LeapYear

#Test for Leap Year
class TestLeapYear(unittest.TestCase):

    def test_non_leap(self):
        self.assertEqual(LeapYear.calc_Leap(2005),"No")

if __name__ == "__main__":
    unittest.main()