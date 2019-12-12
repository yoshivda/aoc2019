import unittest
from .solution import solve1, solve2


class TestSuite(unittest.TestCase):
    def test_1(self):
        self.assertEqual(179, solve1("day12/test1.txt", 10))

    def test_2(self):
        self.assertEqual(1940, solve1("day12/test2.txt", 100))

    def test_3(self):
        self.assertEqual(2772, solve2("day12/test1.txt"))

    def test_4(self):
        self.assertEqual(4686774924, solve2("day12/test2.txt"))


if __name__ == "__main__":
    unittest.main()
