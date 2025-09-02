import unittest
from main import add_numbers, is_even, calculate_factorial


class TestMain(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)
        self.assertEqual(add_numbers(1.5, 2.5), 4.0)
    
    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-1))
        self.assertTrue(is_even(-2))
    
    def test_calculate_factorial(self):
        self.assertEqual(calculate_factorial(0), 1)
        self.assertEqual(calculate_factorial(1), 1)
        self.assertEqual(calculate_factorial(5), 120)
        self.assertEqual(calculate_factorial(3), 6)
    
    def test_calculate_factorial_negative(self):
        with self.assertRaises(ValueError):
            calculate_factorial(-1)


if __name__ == '__main__':
    unittest.main()
