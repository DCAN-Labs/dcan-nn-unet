from scipy.spatial import distance

def directed_hausdorff_distance(X, Y):
    return max([min([distance.euclidean(x, y) for y in Y]) for x in X])

def hausdorff_distance(X, Y):
    return max(directed_hausdorff_distance(X, Y), directed_hausdorff_distance(Y, X))
