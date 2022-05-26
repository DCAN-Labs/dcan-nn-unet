import os
from os import listdir
from os.path import isfile, join
import shutil


def is_t1_file(f):
    return f[-12:-7] == '_0000'


for i in range(10):
    nnunet_raw_data_base_dir = '/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base'
    nnunet_raw_data_dir = os.path.join(nnunet_raw_data_base_dir, 'nnUNet_raw_data')
    t1_folder = os.path.join(nnunet_raw_data_dir, f'Task{str(530 + i)}_T1_Fold{str(i)}')
    if not os.path.exists(t1_folder):
        os.makedirs(t1_folder)

    # imagesTr
    t1_images_tr_folder = os.path.join(t1_folder, 'imagesTr')
    if not os.path.exists(t1_images_tr_folder):
        os.makedirs(t1_images_tr_folder)
    # /home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task516_Paper_Fold0/imagesTr/
    fold_dir_prefix = f'Task{516 + i}_Paper_Fold{i}'
    src_dir = os.path.join(nnunet_raw_data_dir, fold_dir_prefix, 'imagesTr')
    only_files = [f for f in listdir(src_dir) if isfile(join(src_dir, f))]
    for f in only_files:
        if is_t1_file(f):
            shutil.copy(join(src_dir, f), t1_images_tr_folder)

    # imagesTs
    t1_images_ts_folder = os.path.join(t1_folder, 'imagesTs')
    if not os.path.exists(t1_images_ts_folder):
        os.makedirs(t1_images_ts_folder)
    src_dir = os.path.join(nnunet_raw_data_dir, fold_dir_prefix, 'imagesTs')
    only_files = [f for f in listdir(src_dir) if isfile(join(src_dir, f))]
    for f in only_files:
        if is_t1_file(f):
            shutil.copy(join(src_dir, f), t1_images_ts_folder)

    # labelsTr
    t1_labels_tr_folder = os.path.join(t1_folder, 'labelsTr')
    if not os.path.exists(t1_labels_tr_folder):
        os.makedirs(t1_labels_tr_folder)
    src_dir = os.path.join(nnunet_raw_data_dir, fold_dir_prefix, 'labelsTr')
    only_files = [f for f in listdir(src_dir) if isfile(join(src_dir, f))]
    for f in only_files:
        shutil.copy(join(src_dir, f), t1_labels_tr_folder)
