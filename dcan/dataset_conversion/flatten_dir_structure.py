import os
import shutil
import sys
from os.path import join
from shutil import copyfile

from tqdm import tqdm
from os import listdir
from os.path import isfile, join


def flatten_dir_structure(src_dir, dest_dir):
    dirs = [f for f in os.listdir(src_dir) if os.path.isdir(os.path.join(src_dir, f))]
    for dir in tqdm(dirs):
        subject = dir[-6:]
        print(f'subject: {subject}')
        subject_dir = os.path.join(src_dir, dir)
        ses_dirs = [f for f in os.listdir(subject_dir) if os.path.isdir(os.path.join(subject_dir, f))]
        for ses_dir in tqdm(ses_dirs):
            age = ses_dir[-3:]
            print(f'age {age}')
            anat_folder = os.path.join(subject_dir, ses_dir, 'anat')
            anat_files = [f for f in listdir(anat_folder) if isfile(join(anat_folder, f))]
            for anat_file in tqdm(anat_files):
                print(f'anat_file: {anat_file}')
                source_file = os.path.join(anat_folder, anat_file)
                images_tr_folder = os.path.join(dest_dir, 'imagesTr')
                base_name = f'{age}_{subject}'
                if 'T1' in anat_file:
                    new_file = os.path.join(images_tr_folder, f'{base_name}_0000.nii.gz')
                elif 'T2' in anat_file:
                    new_file = os.path.join(images_tr_folder, f'{base_name}_0001.nii.gz')
                else:
                    new_file = os.path.join(dest_dir, 'labelsTr', f'{base_name}.nii.gz')
                shutil.move(source_file, new_file)


if __name__ == "__main__":
    flatten_dir_structure(sys.argv[1], sys.argv[2])
