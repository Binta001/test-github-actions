#!/usr/bin/env python3
"""
Unit tests for the Calculator Application
"""
import unittest
from app import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""
    
    def test_add(self):
        """Test addition function."""
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -3), -8)
    
    def test_subtract(self):
        """Test subtraction function."""
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(-3, -3), 0)
    
    def test_multiply(self):
        """Test multiplication function."""
        self.assertEqual(multiply(6, 7), 42)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 100), 0)
    
    def test_divide(self):
        """Test division function."""
        self.assertEqual(divide(15, 3), 5)
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(7, 2), 3.5)
    
    def test_divide_by_zero(self):
        """Test division by zero raises an error."""
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
