from scipy.spatial import distance

def one_side_hausdorff(x, Y):
    return min([distance.euclidean(x, y) for y in Y])

def hausdorff_distance(X, Y):
    return max([one_side_hausdorff(x, Y) for x in X] + [one_side_hausdorff(y, X) for y in Y])
