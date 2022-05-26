import os
from os import listdir
from os.path import isfile, join
import shutil

from dcan.dataset_conversion.rename_t2_files import rename_t2_files
from dcan.paper.setup_single_modality_folders import setup_images_tr_folder


def is_t2_file(f):
    return f[-12:-7] == '_0001'


for i in range(10):
    nnunet_raw_data_base_dir = '/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base'
    nnunet_raw_data_dir = os.path.join(nnunet_raw_data_base_dir, 'nnUNet_raw_data')
    t2_folder = os.path.join(nnunet_raw_data_dir, f'Task{str(540 + i)}_T1_Fold{str(i)}')
    if not os.path.exists(t2_folder):
        os.makedirs(t2_folder)
    fold_dir_prefix = f'Task{516 + i}_Paper_Fold{i}'

    # imagesTr
    setup_images_tr_folder(t2_folder, is_t2_file, nnunet_raw_data_dir, True, fold_dir_prefix)

    # imagesTs
    # TODO Factor out duplicate code.
    t2_images_ts_folder = os.path.join(t2_folder, 'imagesTs')
    if not os.path.exists(t2_images_ts_folder):
        os.makedirs(t2_images_ts_folder)
    src_dir = os.path.join(nnunet_raw_data_dir, fold_dir_prefix, 'imagesTs')
    only_files = [f for f in listdir(src_dir) if isfile(join(src_dir, f))]
    for f in only_files:
        if is_t2_file(f):
            shutil.copy(join(src_dir, f), t2_images_ts_folder)
    rename_t2_files(t2_images_ts_folder)

    # labelsTr
    # TODO Factor out duplicate code.
    t2_labels_tr_folder = os.path.join(t2_folder, 'labelsTr')
    if not os.path.exists(t2_labels_tr_folder):
        os.makedirs(t2_labels_tr_folder)
    src_dir = os.path.join(nnunet_raw_data_dir, fold_dir_prefix, 'labelsTr')
    only_files = [f for f in listdir(src_dir) if isfile(join(src_dir, f))]
    for f in only_files:
        shutil.copy(join(src_dir, f), t2_labels_tr_folder)
