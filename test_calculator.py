
"""
https://github.com/Amanda-alm/lab11-AA-ST
Partner 1: Amanda Almeida
Partner 2: Spencer Treadway

"""
import unittest
from calculator import *
class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(1, 0), 1)
        self.assertEqual(add(1, -1), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(sub(1, 1), 0)
        self.assertEqual(sub(1, -1), 2)
        self.assertEqual(sub(3, 5), -2)

    # ##########################

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(multiply(5, 10), 50)
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(-3, 9), -27)

    def test_divide(self):  # 3 assertions
        # Note: This tests the function 'b / a'
        self.assertEqual(div(2, 10), 5.0)  # 10 / 2
        self.assertAlmostEqual(div(5, 2), 0.4)  # 2 / 5
        self.assertAlmostEqual(div(-4, 10), -2.5)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(2, 8), 3)
        self.assertEqual(log(10, 100), 2)
        self.assertEqual(log(2, 0.5), -1)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            log(1, 10)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        # Tests for an invalid argument 'b' (b <= 0)
        # log base 10 of 0 (math.log(0, 10))
        with self.assertRaises(ValueError):
            logarithm(10, 0)

    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5.0)
        self.assertEqual(hypotenuse(5, 12), 13.0)
        self.assertEqual(hypotenuse(0, 10), 10.0)

    def test_sqrt(self):  # 3 assertions
        # Test for invalid argument
        with self.assertRaises(ValueError):
            square_root(-1)
        # Test basic function
        self.assertEqual(square_root(16), 4.0)
        self.assertEqual(square_root(0), 0.0)

# Do not touch this
if __name__ == "__main__":
    unittest.main()