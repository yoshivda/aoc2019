import unittest
from .solution import solve


class TestSuite(unittest.TestCase):
    def test_1(self):
        self.assertEqual(8, solve("day10/test1.txt"))

    def test_2(self):
        self.assertEqual(33, solve("day10/test2.txt"))

    def test_3(self):
        self.assertEqual(35, solve("day10/test3.txt"))

    def test_4(self):
        self.assertEqual(41, solve("day10/test4.txt"))

    def test_5(self):
        self.assertEqual(210, solve("day10/test5.txt"))


if __name__ == "__main__":
    unittest.main()
