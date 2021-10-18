import unittest

from A348301 import numerator, sequence


class Test(unittest.TestCase):

    # See #https://oeis.org/A024451
    def test_numerator(self):
        self.assertEqual(1, numerator(1))
        self.assertEqual(5, numerator(2))
        self.assertEqual(31, numerator(3))
        self.assertEqual(247, numerator(4))

    def test_sequence(self):
        self.assertEqual(-1, sequence(1))
        self.assertEqual(-1, sequence(2))
        self.assertEqual(1, sequence(3))
        self.assertEqual(37, sequence(4))
        self.assertEqual(617, sequence(5))
        self.assertEqual(10331, sequence(6))


if __name__ == '__main__':
    unittest.main()
