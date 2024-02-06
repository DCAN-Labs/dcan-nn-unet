import os.path
import shutil
from os import listdir
from os.path import isfile, join

t1_task_number = 530
all_task_number = 540
nnUNet_raw_data_folder = '/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data'
sub_folders = ['imagesTr', 'imagesTs', 'labelsTr', 'labelsTs']
for fold in range(10):
    src_folder = os.path.join(nnUNet_raw_data_folder, f'Task{t1_task_number}_T1_only_Fold{fold}/')
    dest_folder = os.path.join(nnUNet_raw_data_folder, f'Task{all_task_number}_both_Fold{fold}/')
    is_exist = os.path.exists(dest_folder)
    if not is_exist:
        os.makedirs(dest_folder, exist_ok=True)
    for sub_folder in sub_folders:
        shutil.copytree(os.path.join(src_folder, sub_folder), os.path.join(dest_folder, sub_folder))
    images_folders = ['imagesTr', 'imagesTs']
    for image_folder in images_folders:
        dest_images_folder = os.path.join(dest_folder, image_folder)
        only_files = [f for f in listdir(dest_images_folder) if isfile(join(dest_images_folder, f))]
        for t1_file in only_files:
            t2_file = t1_file.replace('_0000.nii.gz', '_0001.nii.gz')
            task530_549_all_dir = '/home/feczk001/shared/data/nnUNet/raw_data/Task530_549_all'
            if t2_file.startswith("SynthSeg"):
                src_folder = os.path.join(task530_549_all_dir, 'SynthSeg')
            else:
                src_folder = os.path.join(task530_549_all_dir, 'real_images')
            src = os.path.join(src_folder, t2_file)
            dst = os.path.join(dest_images_folder, t2_file)
            shutil.copyfile(src, dst)

    t1_task_number += 1
    all_task_number += 1
