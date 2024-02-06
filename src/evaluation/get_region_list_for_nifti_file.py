# Author: Paul Reiners

import sys
from sortedcontainers import SortedSet

import nibabel as nib


def get_regions(filename):
    img = nib.load(filename)
    data = img.get_fdata()
    regions = SortedSet()
    max_x = data.shape[0]
    max_y = data.shape[1]
    max_z = data.shape[2]
    for i in range(max_x):
        for j in range(max_y):
            for k in range(max_z):
                region = int(data[i][j][k])
                regions.add(region)

    return regions


def main(filename):
    return get_regions(filename)


if __name__ == "__main__":
    filename = sys.argv[1]
    result = main(filename)
    print('Regions: ', result)
