import os
import sys
from os.path import join
from shutil import copyfile


def flatten_dir_structure(src_dir, dest_dir):
    for root, dirs, files in os.walk(src_dir):
        path = root.split(os.sep)
        print((len(path) - 1) * '---', os.path.basename(root))
        for file in files:
            print(len(path) * '---', file)
            suffix = ''
            if 'T1' in file:
                new_file = file.replace('T1w', '0000')
            elif 'T2' in file:
                new_file = file.replace('T2w', '0001')
            new_file_name = path[-2] + '_' + path[-1] + new_file
            current_src_dir = '/'.join(path)
            src = join(current_src_dir, file)
            dst = join(dest_dir, new_file_name)
            copyfile(src, dst)


if __name__ == "__main__":
    flatten_dir_structure(sys.argv[1], sys.argv[2])
