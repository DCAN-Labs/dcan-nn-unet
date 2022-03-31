from unittest import TestCase
import numpy as np
from scipy.spatial import distance

from dcan.paper.hausdorff_distance import hausdorff_distance


class HausdorffDistanceTest(TestCase):
    def test_hausdorff_distance(self):
        X = [(np.random.uniform(), np.random.uniform(), np.random.uniform()) for i in range(100)]
        Y = [(np.random.uniform(0.5, 1.5), np.random.uniform(0.5, 1.5), np.random.uniform(0.5, 1.5)) for i in range(100)]
        actual = hausdorff_distance(X, Y)
        d1, _, _ = distance.directed_hausdorff(X, Y)
        d2, _, _ = distance.directed_hausdorff(Y, X)
        expected = max([d1, d2])
        self.assertAlmostEqual(expected, actual)

    def test_hausdorff_distance_almost_equal(self):
        X = [(np.random.uniform(), np.random.uniform(), np.random.uniform()) for i in range(100)]
        Y = [(np.random.uniform(0.0001, 1.0001), np.random.uniform(0.0001, 1.0001), np.random.uniform(0.0001, 1.0001)) for i in range(100)]
        actual = hausdorff_distance(X, Y)
        d1, _, _ = distance.directed_hausdorff(X, Y)
        d2, _, _ = distance.directed_hausdorff(Y, X)
        expected = max([d1, d2])
        self.assertAlmostEqual(expected, actual)
