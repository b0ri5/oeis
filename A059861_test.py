import unittest

from A059861 import brute_force


class Test(unittest.TestCase):

    # See https://oeis.org/A059861
    def test_brute_force(self):
        self.assertEqual(1, brute_force(1))
        self.assertEqual(1, brute_force(2))
        self.assertEqual(3, brute_force(3))
        self.assertEqual(15, brute_force(4))
        self.assertEqual(135, brute_force(5))
        self.assertEqual(1485, brute_force(6))


if __name__ == '__main__':
    unittest.main()
