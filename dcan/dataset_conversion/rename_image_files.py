import sys
from os import listdir
from os.path import isfile, join
import os


def main(image_dir):
    image_files = sorted([f for f in listdir(image_dir) if isfile(join(image_dir, f))])
    n = len(image_files)
    for i in range(n):
        image_file = image_files[i]
        # Get rid of ".nii.gz" extension
        image_file_base = image_file[:-7]
        if 'T1w_' in image_file_base:
            new_image_file_base = image_file_base.replace('T1w_', '')
            new_image_file_name = new_image_file_base + "_0000.nii.gz"
        else:
            new_image_file_base = image_file_base.replace('T2w_', '')
            new_image_file_name = new_image_file_base + "_0001.nii.gz"

        os.rename(image_dir + '/' + image_file, image_dir + '/' + new_image_file_name)


if __name__ == "__main__":
    main(sys.argv[1])
