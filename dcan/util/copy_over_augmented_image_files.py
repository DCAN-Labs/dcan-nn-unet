import os
from shutil import copyfile
import sys


def copy_over_augmented_image_files(source_directory, images_tr_directory, labels_tr_directory):
    files = os.listdir(source_directory)

    for f in files:
        #print(f)
        if f.endswith('_0000.nii.gz') or f.endswith('_0001.nii.gz'):
            dst = images_tr_directory
        else:
            dst = labels_tr_directory
        src = os.path.join(source_directory, f)
        dst_path = os.path.join(dst, f)
        copyfile(src, dst_path)


if __name__ == "__main__":
    copy_over_augmented_image_files(sys.argv[1], sys.argv[2], sys.argv[3])
