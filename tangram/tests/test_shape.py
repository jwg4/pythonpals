import unittest

import numpy as np

from Tangram import Square, rotate


class TestSquare(unittest.TestCase):
    def setUp(self):
        """ create an example square which we will use for all the tests."""
        self.square = Square(
            np.array([0, 0]),
            np.array([1, 0]),
            np.array([1, 1]),
            np.array([0, 1])
        )

    def test_rotate(self):
        rotate(self.square, 90)
        np.testing.assert_array_equal(self.square.point1, np.array([0, 0]))
