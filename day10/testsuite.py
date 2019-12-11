import unittest
from .solution import solve1, solve2


class TestSuite(unittest.TestCase):
    def test_1(self):
        self.assertEqual(8, solve1("day10/test1.txt"))

    def test_2(self):
        self.assertEqual(33, solve1("day10/test2.txt"))

    def test_3(self):
        self.assertEqual(35, solve1("day10/test3.txt"))

    def test_4(self):
        self.assertEqual(41, solve1("day10/test4.txt"))

    def test_5(self):
        self.assertEqual(210, solve1("day10/test5.txt"))

    def test_6(self):
        self.assertEqual((11, 12), solve2("day10/test5.txt")[0])

    def test_7(self):
        self.assertEqual((12, 1), solve2("day10/test5.txt")[1])

    def test_8(self):
        self.assertEqual((12, 2), solve2("day10/test5.txt")[2])

    def test_9(self):
        self.assertEqual((12, 8), solve2("day10/test5.txt")[9])

    def test_10(self):
        self.assertEqual((16, 0), solve2("day10/test5.txt")[19])

    def test_11(self):
        self.assertEqual((16, 9), solve2("day10/test5.txt")[49])

    def test_12(self):
        self.assertEqual((10, 16), solve2("day10/test5.txt")[99])

    def test_13(self):
        self.assertEqual((9, 6), solve2("day10/test5.txt")[199])


if __name__ == "__main__":
    unittest.main()
