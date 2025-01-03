import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1,-1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(2,5), -3)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
    
    def test_power(self):
        self.assertEqual(power(2,3), 8)
        self.assertEqual(power(2,0), 1)

    def test_square_root(self):
        self.assertEqual(square_root(9), 3)
        with self.assertRaises(ValueError):
            square_root(-1)

    def test_percentage(self):
        self.assertEqual(percentage(50, 100), 50)
        self.assertEqual(percentage(10, 200), 20)

    def test_memory_functions(self):
        memory_store(5)
        self.assertEqual(memory_recall(), 5)
        memory_add(5)
        self.assertEqual(memory_recall(), 10)
        memory_subtract(3)
        self.assertEqual(memory_recall(), 7)
        memory_clear()
        self.assertEqual(memory_recall(), 0)


if __name__ == '__main__':
    unittest.main()