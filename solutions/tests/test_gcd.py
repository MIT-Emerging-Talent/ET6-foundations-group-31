import unittest

from ..greatest_common_divisor import gcd


class TestGCD(unittest.TestCase):
    def test_gcd_positive_numbers(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(54, 24), 6)
        self.assertEqual(gcd(101, 103), 1)

    def test_gcd_with_zero(self):
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(5, 0), 5)
        self.assertEqual(gcd(0, 0), 0)

    def test_gcd_negative_numbers(self):
        self.assertEqual(gcd(-48, 18), 6)
        self.assertEqual(gcd(48, -18), 6)
        self.assertEqual(gcd(-48, -18), 6)

    def test_gcd_same_numbers(self):
        self.assertEqual(gcd(7, 7), 7)
        self.assertEqual(gcd(100, 100), 100)

    def test_gcd_one_is_multiple_of_other(self):
        self.assertEqual(gcd(12, 36), 12)
        self.assertEqual(gcd(36, 12), 12)


if __name__ == "__main__":
    unittest.main()
