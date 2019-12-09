import unittest
from .solution import solve1, solve2


class TestSuite(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, solve1("day8/test1.txt", 3, 2))

    def test_2(self):
        self.assertEqual("0110", solve2("day8/test2.txt", 2, 2))


if __name__ == "__main__":
    unittest.main()
