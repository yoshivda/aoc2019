import unittest
from .solution import solve


class TestSuite(unittest.TestCase):

    def test_1(self):
        self.assertEqual([2,0,0,0,99], solve("day2/test1.txt"))

    def test_2(self):
        self.assertEqual([2,3,0,6,99], solve("day2/test2.txt"))

    def test_3(self):
        self.assertEqual([2,4,4,5,99,9801], solve("day2/test3.txt"))

    def test_4(self):
        self.assertEqual([30,1,1,4,2,5,6,0,99], solve("day2/test4.txt"))

    def test_5(self):
        self.assertEqual([3500,9,10,70,2,3,11,0,99,30,40,50], solve("day2/test5.txt"))


if __name__ == "__main__":
    unittest.main()
