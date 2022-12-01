import os
from os import listdir
from os.path import isfile, join

root_dir = '/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task550/'
month_dirs = os.listdir(path=root_dir)
for month_dir in month_dirs:
    month_path = os.path.join(root_dir, month_dir)
    if os.path.isdir(month_path):
        sub_dirs = os.listdir(path=month_path)
        for sub_dir in sub_dirs:
            sub_path = os.path.join(month_path, sub_dir)
            only_files = [f for f in listdir(sub_path) if isfile(join(sub_path, f))]
            assert len(only_files) == 0
            os.rmdir(sub_path)
        os.rmdir(month_path)
