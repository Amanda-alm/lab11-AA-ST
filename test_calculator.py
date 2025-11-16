#https://github.com/Amanda-alm/lab11-AA-ST
#Partner 1: Amanda Almeida
#Partner 2: Spencer Treadway

"""
https://github.com/Amanda-alm/lab11-AA-ST
Partner 1: Amanda Almeida
Partner 2: Spencer Treadway

"""
import unittest
from calculator imp
class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(multiply(5, 10), 50)
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(-3, 9), -27)

    def test_divide(self):  # 3 assertions
        # Note: This tests the function 'b / a'
        self.assertEqual(divide(2, 10), 5.0)  # 10 / 2
        self.assertAlmostEqual(divide(5, 2), 0.4)  # 2 / 5
        self.assertAlmostEqual(divide(-4, 10), -2.5)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
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