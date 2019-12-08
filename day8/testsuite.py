import unittest
from .solution import solve


class TestSuite(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, solve("day8/test1.txt", 3, 2))


if __name__ == "__main__":
    unittest.main()
