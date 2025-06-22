import unittest

def add(x, y):
    return x + y
# We define individual tests as test cases within a TestCase class.
class TestAdd(unittest.TestCase):
# Each test case has a specific method named with test_ followed by a descriptive name
    def test_add_positive(self):
        result = add(5,3)
        self.assertEqual(result, 8)

    def test_addnegative(self):
        result = add(-2, 7)
        """ Assert the expected outcome using 
        self.assertEqual(actual, expected)"""
        self.assertEqual(result, 5)

if __name__ == "__main__":
    unittest.main()

    # Exercise 1: Understanding the Importance of Testing
    Exercise 1: Understanding the Importance of Testing

Instruction:

Write a small Python function (e.g., a function to calculate the square of a number) and intentionally introduce a bug (e.g., incorrect calculation logic).