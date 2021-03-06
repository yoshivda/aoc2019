import unittest
from .solution import solve


class TestSuite(unittest.TestCase):
    def test_1(self):
        self.assertEqual(610, solve("day3/test1.txt"))

    def test_2(self):
        self.assertEqual(410, solve("day3/test2.txt"))

    def test_3(self):
        self.assertEqual(30, solve("day3/test3.txt"))


if __name__ == "__main__":
    unittest.main()
