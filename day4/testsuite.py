import unittest
from .solution import is_valid_pt1, is_valid_pt2


class TestSuite(unittest.TestCase):
    def test_pt1_1(self):
        self.assertTrue(is_valid_pt1(111111))

    def test_pt1_2(self):
        self.assertFalse(is_valid_pt1(223450))

    def test_pt1_3(self):
        self.assertFalse(is_valid_pt1(123789))

    def test_pt2_1(self):
        self.assertTrue(is_valid_pt2(112233))

    def test_pt2_2(self):
        self.assertFalse(is_valid_pt2(123444))

    def test_pt2_3(self):
        self.assertTrue(is_valid_pt2(111122))


if __name__ == "__main__":
    unittest.main()
