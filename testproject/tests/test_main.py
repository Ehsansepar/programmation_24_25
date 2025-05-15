import unittest
import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import sum2Num

class TestMainFunctions(unittest.TestCase):
    def test_sum2Num(self):
        self.assertEqual(sum2Num(2, 3), 5)
        self.assertEqual(sum2Num(-1, 1), 0)
        self.assertEqual(sum2Num(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
