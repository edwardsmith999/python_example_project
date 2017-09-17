from number_fns import square, cube
import unittest

class test_square(unittest.TestCase):
    def test_float(self):
        self.assertEqual(square(2.), 4.)
        self.assertEqual(cube(2.), 8.)
    def test_int(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(cube(2), 8)

unittest.main(argv=['first-arg-is-ignored'], exit=False)
