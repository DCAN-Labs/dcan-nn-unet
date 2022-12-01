import os
from os import listdir
from os.path import isfile, join
import shutil


root_dir = '/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task550/'
month_dirs = os.listdir(path=root_dir)
for month_dir in month_dirs:
    month_path = os.path.join(root_dir, month_dir)
    sub_dirs = os.listdir(path=month_path)
    for sub_dir in sub_dirs:
        sub_path = os.path.join(month_path, sub_dir)
        only_files = [f for f in listdir(sub_path) if isfile(join(sub_path, f))]
        for f in only_files:
            f_path = os.path.join(sub_path, f)
            print(f_path)
            base_name = f'{month_dir}_{sub_dir}'
            if 'T1w' in f:
                dest_file = os.path.join(root_dir, f'{base_name}_0000.nii.gz')
            elif 'T2w' in f:
                dest_file = os.path.join(root_dir, f'{base_name}_0001.nii.gz')
            else:
                dest_file = os.path.join(root_dir, f'{base_name}.nii.gz')
            print(dest_file)
            shutil.move(f_path, dest_file)
