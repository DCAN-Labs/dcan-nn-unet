import os
from os import listdir
from os.path import isfile, join
import shutil


root_dir = '/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task550/'
root_src_dir = '/home/miran045/reine097/Downloads/0mo/'
template_dirs = os.listdir(path=root_src_dir)
for template_dir in template_dirs:
    template_path = os.path.join(root_src_dir, template_dir)
    only_files = [f for f in listdir(template_path) if isfile(join(template_path, f))]
    for f in only_files:
        f_path = os.path.join(template_path, f)
        print(f_path)
        base_name = f'0mo_{template_dir}'
        if 'T1w' in f:
            dest_file = os.path.join(root_dir, f'{base_name}_0000.nii.gz')
        elif 'T2w' in f:
            dest_file = os.path.join(root_dir, f'{base_name}_0001.nii.gz')
        else:
            dest_file = os.path.join(root_dir, f'{base_name}.nii.gz')
        print(dest_file)
        shutil.move(f_path, dest_file)
        print()
