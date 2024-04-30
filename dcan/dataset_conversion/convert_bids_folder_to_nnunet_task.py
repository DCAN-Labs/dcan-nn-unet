import os.path
import shutil
from glob import glob
from os.path import abspath, join, isdir, isfile

from tqdm import tqdm

source_folder = '/scratch.global/reine097/nnUNet/s3_bucket_backup'
task_folder = '/scratch.global/reine097/Task526/'
images_tr_folder = os.path.join(task_folder, 'imagesTr')
labels_tr_folder = os.path.join(task_folder, 'labelsTr')
for month in tqdm(range(1, 9)):
    data_path = os.path.join(source_folder, f'{month}mo')
    sub_folders = [abspath(d) for d in glob(join(data_path, '*')) if isdir(d)]
    for sub_folder in sub_folders:
        subject_id = sub_folder[-6:]
        files = [abspath(f) for f in glob(join(sub_folder, '*')) if isfile(f)]
        segmentation_file = None
        t1_file = None
        t2_file = None
        for f in files:
            if f.endswith('dseg.nii.gz'):
                segmentation_file = f
            elif f.endswith('_T1w.nii.gz'):
                t1_file = f
            else:
                t2_file = f
        file_prefix = f'{month}mo_{subject_id}'
        shutil.copyfile(segmentation_file, os.path.join(labels_tr_folder, f'{file_prefix}.nii.gz'))
        shutil.copyfile(t1_file, os.path.join(images_tr_folder, f'{file_prefix}_0000.nii.gz'))
        shutil.copyfile(t2_file, os.path.join(images_tr_folder, f'{file_prefix}_0001.nii.gz'))
