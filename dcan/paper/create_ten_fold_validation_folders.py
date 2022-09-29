# create_ten_fold_validation_folders.py
# Author: Paul Reiners

import sys
import os.path
from os import listdir
from os.path import isfile, join
from shutil import copyfile

from sklearn.model_selection import StratifiedKFold


def move_file_unit(
        indices, all_images, source_folder, dest_images_folder, dest_labels_folder, include_t1=True, include_t2=True):
    for i in indices:
        base_file_name = all_images[i]
        if include_t1:
            t1_src_file = base_file_name + '_0000.nii.gz'
            copyfile(os.path.join(source_folder, t1_src_file), os.path.join(dest_images_folder, t1_src_file))
        if include_t2:
            t2_src_file = base_file_name + '_0001.nii.gz'
            copyfile(os.path.join(source_folder, t2_src_file), os.path.join(dest_images_folder, t2_src_file))
        label_src_file = base_file_name + '.nii.gz'
        copyfile(os.path.join(source_folder, label_src_file), os.path.join(dest_labels_folder, label_src_file))


def create_ten_fold_validation_folders(
        source_folder, starting_task_number, task_name, classifier_func, include_t1=True, include_t2=True):
    nnunet_raw_data_folder = '/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data'
    all_images = [f for f in listdir(source_folder) if isfile(join(source_folder, f))]
    all_images.sort()
    all_images = all_images[::3]
    all_images = list(set([f[:-7] for f in all_images]))
    classes = [classifier_func(f) for f in all_images]
    skf = StratifiedKFold(n_splits=10)
    fold = 0
    splits = skf.split(all_images, classes)
    for train, test in splits:
        full_task_name = f'Task{starting_task_number}_{task_name}_Fold{str(fold)}'
        task_folder_name = os.path.join(nnunet_raw_data_folder, full_task_name)
        if not os.path.exists(task_folder_name):
            os.mkdir(task_folder_name)
        dest_images_tr_folder = os.path.join(task_folder_name, "imagesTr")
        if not os.path.exists(dest_images_tr_folder):
            os.mkdir(dest_images_tr_folder)
        dest_images_ts_folder = os.path.join(task_folder_name, "imagesTs")
        if not os.path.exists(dest_images_ts_folder):
            os.mkdir(dest_images_ts_folder)
        dest_labels_tr_folder = os.path.join(task_folder_name, "labelsTr")
        if not os.path.exists(dest_labels_tr_folder):
            os.mkdir(dest_labels_tr_folder)
        dest_labels_ts_folder = os.path.join(task_folder_name, "labelsTs")
        if not os.path.exists(dest_labels_ts_folder):
            os.mkdir(dest_labels_ts_folder)
        move_file_unit(
            train, all_images, source_folder, dest_images_tr_folder, dest_labels_tr_folder, include_t1, include_t2)
        move_file_unit(
            test, all_images, source_folder, dest_images_ts_folder, dest_labels_ts_folder, include_t1, include_t2)
        starting_task_number += 1
        fold += 1


def main() -> int:
    """Create stratified 10-fold validation folders"""
    folder = sys.argv[1]
    task_number = int(sys.argv[2])
    task_name = sys.argv[3]
    synth_seg = bool(sys.argv[4])
    include_t1 = bool(sys.argv[5])
    include_t2 = bool(sys.argv[6])
    if synth_seg:
        def classifier_func(f):
            last_underscore_pos = f.rfind('_')

            return int(f[last_underscore_pos + 1:]) % 10
    else:
        def classifier_func(f): return int(f[0])

    create_ten_fold_validation_folders(folder, task_number, task_name, classifier_func, include_t1, include_t2)

    return 0


if __name__ == '__main__':
    sys.exit(main())
