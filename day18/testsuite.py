import unittest
from .solution import solve


class TestSuite(unittest.TestCase):
    def test_1(self):
        self.assertEqual(8, solve("day18/test1.txt"))

    def test_2(self):
        self.assertEqual(86, solve("day18/test2.txt"))

    def test_3(self):
        self.assertEqual(132, solve("day18/test3.txt"))

    def test_4(self):
        self.assertEqual(136, solve("day18/test4.txt"))

    def test_5(self):
        self.assertEqual(81, solve("day18/test5.txt"))


if __name__ == "__main__":
    unittest.main()
