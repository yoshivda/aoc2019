import unittest
from .solution import solve


class TestSuite(unittest.TestCase):
    def test_1(self):
        self.assertEqual(2, solve("day1/test1.txt"))

    def test_2(self):
        self.assertEqual(966, solve("day1/test2.txt"))

    def test_3(self):
        self.assertEqual(50346, solve("day1/test3.txt"))


if __name__ == "__main__":
    unittest.main()
