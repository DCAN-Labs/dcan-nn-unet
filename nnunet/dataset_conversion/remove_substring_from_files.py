import os
import sys
from os import listdir
from os.path import isfile, join


def main(fldr):
    onlyfiles = [f for f in listdir(fldr) if isfile(join(fldr, f))]
    for file_name in onlyfiles:
        new_file_name = file_name
        if '_T1w' in file_name:
            new_file_name = file_name.replace('_T1w', '')
        if '_T2w' in file_name:
            new_file_name = file_name.replace('_T2w', '')
        file = join(fldr, file_name)
        destination = join(fldr, new_file_name)
        os.rename(file, destination)


if __name__ == "__main__":
    folder = sys.argv[1]
    main(folder)
