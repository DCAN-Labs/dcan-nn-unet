# Author: Paul Reiners

from os import listdir
from os.path import isfile, join
import os
import sys


def rename_t2_files(folder_name):
    files = [join(folder_name, f) for f in listdir(folder_name) if isfile(join(folder_name, f))]
    for f in files:
        new_f = f.replace('_0001', '_0000')
        os.rename(f, new_f)


if __name__ == '__main__':
    rename_t2_files(sys.argv[1])
