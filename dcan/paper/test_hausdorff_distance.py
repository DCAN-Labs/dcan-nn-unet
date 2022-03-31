from unittest import TestCase
import numpy as np
from scipy.spatial import distance

from dcan.paper.hausdorff_distance import hausdorff_distance, directed_hausdorff_distance


class HausdorffDistanceTest(TestCase):
    def test_hausdorff_distance(self):
        X = [(np.random.uniform(), np.random.uniform(), np.random.uniform()) for i in range(100)]
        Y = [(np.random.uniform(0.5, 1.5), np.random.uniform(0.5, 1.5), np.random.uniform(0.5, 1.5)) for i in range(100)]
        actual = hausdorff_distance(X, Y)
        d1, _, _ = distance.directed_hausdorff(X, Y)
        d2, _, _ = distance.directed_hausdorff(Y, X)
        expected = max([d1, d2])
        print(expected, actual)
        self.assertAlmostEqual(expected, actual)

    def test_hausdorff_distance_almost_equal(self):
        X = [(np.random.uniform(), np.random.uniform(), np.random.uniform()) for i in range(100)]
        Y = [(np.random.uniform(0.0000, 1.0000), np.random.uniform(0.00001, 1.00001), np.random.uniform(0.0001, 1.0001)) for i in range(10000)]
        actual = hausdorff_distance(X, Y)
        d1, _, _ = distance.directed_hausdorff(X, Y)
        d2, _, _ = distance.directed_hausdorff(Y, X)
        expected = max([d1, d2])
        print(expected, actual)
        self.assertAlmostEqual(expected, actual)

    def test_hausdorff_distance_equal(self):
        X = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
        Y = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
        actual = hausdorff_distance(X, Y)
        d1, _, _ = distance.directed_hausdorff(X, Y)
        d2, _, _ = distance.directed_hausdorff(Y, X)
        expected = max([d1, d2])
        print(expected, actual)
        self.assertAlmostEqual(expected, actual)

    def test_directed_hausdorff_distance(self):
        X = [(np.random.uniform(), np.random.uniform(), np.random.uniform()) for i in range(100)]
        Y = [(np.random.uniform(0.5, 1.5), np.random.uniform(0.5, 1.5), np.random.uniform(0.5, 1.5)) for i in range(100)]
        actual = directed_hausdorff_distance(X, Y)
        expected, _, _ = distance.directed_hausdorff(X, Y)
        print(expected, actual)
        self.assertAlmostEqual(expected, actual)

    def test_directed_hausdorff_distance_almost_equal(self):
        X = [(np.random.uniform(), np.random.uniform(), np.random.uniform()) for i in range(100)]
        Y = [(np.random.uniform(0.0000, 1.0000), np.random.uniform(0.00001, 1.00001), np.random.uniform(0.0001, 1.0001)) for i in range(10000)]
        actual = directed_hausdorff_distance(X, Y)
        expected, _, _ = distance.directed_hausdorff(X, Y)
        print(expected, actual)
        self.assertAlmostEqual(expected, actual)

    def test_directed_hausdorff_distance_equal(self):
        X = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
        Y = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
        actual = directed_hausdorff_distance(X, Y)
        expected, _, _ = distance.directed_hausdorff(X, Y)
        print(expected, actual)
        self.assertAlmostEqual(expected, actual)
