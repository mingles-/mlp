from unittest import TestCase
import numpy
import unittest
from numpy.testing import assert_array_almost_equal
from mlp.layers import Sigmoid, Softmax

__author__ = 'mingles'


class Tests(TestCase):

    # def test_sigmoid(self):
    #     s = Sigmoid()
    #     actual = s.sigmoid(50.0)
    #     self.assertAlmostEqual(actual, 1)


    # def test_softmax_array(self):
    #     """ Ensure that a softmax gives the correct output """
    #
    #     actual = Softmax.softmax(numpy.asarray([[0.0, 100.0], [100.0, 0.0]]))
    #     print actual
    #     expected = numpy.asarray([[0.0, 1.0], [1.0, 0.0]])
    #     print expected
    #     assert_array_almost_equal(expected, actual, decimal=3)
    #
    # def test_softmax(self):
    #     """ Ensure that a softmax gives the correct output """
    #     actual = Softmax.softmax(numpy.asarray([0.01, 0.01, 10.0]))
    #     expected = numpy.asarray([0.0, 0.0, 1.0])
    #     assert_array_almost_equal(expected, actual, decimal=3)

if __name__ == '__main__':
    unittest.main()