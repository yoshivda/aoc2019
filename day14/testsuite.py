import unittest
from .solution import solve1, read


class TestSuite(unittest.TestCase):
    def test_1(self):
        self.assertEqual(31, solve1(read("day14/test1.txt"), 1))

    def test_2(self):
        self.assertEqual(165, solve1(read("day14/test2.txt"), 1))

    def test_3(self):
        self.assertEqual(13312, solve1(read("day14/test3.txt"), 1))

    def test_4(self):
        self.assertEqual(180697, solve1(read("day14/test4.txt"), 1))

    def test_5(self):
        self.assertEqual(2210736, solve1(read("day14/test5.txt"), 1))


if __name__ == "__main__":
    unittest.main()
