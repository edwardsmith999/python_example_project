import unittest

from python_example_project.number_class import Number

unittest.main(argv=['first-arg-is-ignored'], exit=False)


class test_number(unittest.TestCase):

    def test_float(self):
        n = Number(2.)
        self.assertEqual(n.square(), 4.)
        self.assertEqual(n.cube(), 8.)

    def test_int(self):
        n = Number(2)
        self.assertEqual(n.square(), 4)
        self.assertEqual(n.cube(), 8)

