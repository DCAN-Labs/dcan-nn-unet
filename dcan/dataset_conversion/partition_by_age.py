import os.path
import sys
from os import listdir
from os.path import isfile, join
from pathlib import Path
import shutil

def main(src_dir):
    only_files = [f for f in listdir(src_dir) if isfile(join(src_dir, f))]

    for month in range(9):
        Path(os.path.join(src_dir, f'{month}mo')).mkdir(parents=True, exist_ok=True)

    for f in only_files:
        mo = f[0]
        dest_dir = os.path.join(src_dir, f'{mo}mo')
        shutil.move(join(src_dir, f), dest_dir)

if __name__ == '__main__':
    src_dir = sys.argv[1]
    main(src_dir)
