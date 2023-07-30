
import unittest

# The function we want to test
def add(a, b):
    return a + b

# Test class that inherits from unittest.TestCase
class TestAddFunction(unittest.TestCase):

    # Test case for the add function with two positive integers
    def test_add_positive_numbers(self):
        result = add(5, 3)
        self.assertEqual(result, 8)  # Assertion to check if the result is equal to the expected value

    # Test case for the add function with one positive and one negative integer
    def test_add_positive_and_negative_numbers(self):
        result = add(10, -7)
        self.assertEqual(result, 3)  # Assertion to check if the result is equal to the expected value

    # Test case for the add function with two negative integers
    def test_add_negative_numbers(self):
        result = add(-2, -5)
        self.assertEqual(result, -7)  # Assertion to check if the result is equal to the expected value

if __name__ == '__main__':
    unittest.main()
