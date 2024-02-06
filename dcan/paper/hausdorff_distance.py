from numpy import mean
from scipy.spatial import distance


def directed_hausdorff_distance(X, Y):
    return max([min([distance.euclidean(x, y) for y in Y]) for x in X])


def hausdorff_distance(X, Y):
    return max(directed_hausdorff_distance(X, Y), directed_hausdorff_distance(Y, X))


def directed_hausdorff_distance_95(X, Y):
    min_distances = sorted([min([distance.euclidean(x, y) for y in Y]) for x in X])
    percentile_95_index = int(round(0.95 * len(min_distances)))

    return min_distances[percentile_95_index]


def hausdorff_distance_95(X, Y):
    return max(directed_hausdorff_distance_95(X, Y), directed_hausdorff_distance_95(Y, X))


def directed_mean_distance(X, Y):
    return mean([min([distance.euclidean(x, y) for y in Y]) for x in X])


def mean_distance(X, Y):
    return (directed_mean_distance(X, Y) + directed_mean_distance(Y, X)) / 2.0
