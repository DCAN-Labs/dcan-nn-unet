import os
import sys
from os import listdir
from os.path import isfile, join


def main(fldr, substring):
    onlyfiles = [f for f in listdir(fldr) if isfile(join(fldr, f))]
    for file_name in onlyfiles:
        new_file_name = file_name
        if substring in file_name:
            new_file_name = file_name.replace(substring, '')
        file = join(fldr, file_name)
        destination = join(fldr, new_file_name)
        os.rename(file, destination)


if __name__ == "__main__":
    folder = sys.argv[1]
    main(folder, sys.argv[2])
