import unittest
from .solution import solve


class TestSuite(unittest.TestCase):
    def test_1(self):
        self.assertEqual(23, solve("day20/test1.txt"))

    def test_2(self):
        self.assertEqual(58, solve("day20/test2.txt"))


if __name__ == "__main__":
    unittest.main()
