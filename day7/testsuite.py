import unittest
from .solution import solve


class TestSuite(unittest.TestCase):
    def test_1(self):
        self.assertEqual(43210, solve("day7/test1.txt"))

    def test_2(self):
        self.assertEqual(54321, solve("day7/test2.txt"))

    def test_3(self):
        self.assertEqual(65210, solve("day7/test3.txt"))


if __name__ == "__main__":
    unittest.main()
