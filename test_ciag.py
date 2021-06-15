import unittest
from simpleton import ciag

class TestSum(unittest.TestCase):
    def test_nr_jed(self):
        self.assertEqual(ciag(1), 0)

    def test_nr_dwa(self):
        self.assertEqual(ciag(2), 1)

    def test_nr_trz(self):
        self.assertEqual(ciag(4), 2)

if __name__ == '__main__':
    unittest.main()