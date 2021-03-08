import unittest
import LeapYear

#Test for Leap Year
class TestLeapYear(unittest.TestCase):

    def test_non_leap(self):
        self.assertEqual(LeapYear.calc_Leap(2005),"No")

    def test_non_mult_100(self):
        self.assertEqual(LeapYear.calc_Leap(2100),"No")
    
    def test_non_mult_400(self):
        self.assertEqual(LeapYear.calc_Leap(2400),"Yes")

if __name__ == "__main__":
    unittest.main()