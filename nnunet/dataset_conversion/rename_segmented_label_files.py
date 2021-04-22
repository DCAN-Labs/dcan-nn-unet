import sys
from os import listdir
from os.path import isfile, join
import os


def main(image_dir, label_dir):
    image_files = sorted([f for f in listdir(image_dir) if isfile(join(image_dir, f))])
    label_files = sorted([f for f in listdir(label_dir) if isfile(join(label_dir, f))])
    n = len(image_files)
    if n != len(label_files):
        raise Exception("Different number of image and label files.")
    for i in range(n):
        image_file = image_files[i]
        label_file = label_files[i]
        # Get rid of ".nii.gz" extension
        image_file_base = image_file[:-7]
        label_file_base = label_file[:-7]
        if image_file + '_0000' != label_file:
            max_prefix_len = \
                max([j for j in range(min(len(image_file_base), len(label_file_base))) \
                     if image_file_base[:j] == label_file_base[:j]])
            common_prefix_base = image_file_base[:max_prefix_len]
            if common_prefix_base[-1] == '_':
                common_prefix_base = common_prefix_base[:-1]
            if image_file_base != common_prefix_base:
                os.rename(image_dir + '/' + image_file, image_dir + '/' + common_prefix_base + '_0000.nii.gz')
            if label_file_base != common_prefix_base:
                os.rename(label_dir + '/' + label_file, label_dir + '/' + common_prefix_base + '.nii.gz')


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
