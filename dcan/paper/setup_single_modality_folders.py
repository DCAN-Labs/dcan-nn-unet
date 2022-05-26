import os
import shutil
from os import listdir
from os.path import isfile, join

from dcan.dataset_conversion.rename_t2_files import rename_t2_files


def setup_images_tr_folder(modality_folder, is_modality_file_func, nnunet_raw_data_dir, is_t2_only, fold_dir_prefix):
    images_tr_folder = os.path.join(modality_folder, 'imagesTr')
    if not os.path.exists(images_tr_folder):
        os.makedirs(images_tr_folder)
    # /home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task516_Paper_Fold0/imagesTr/
    src_dir: str = os.path.join(nnunet_raw_data_dir, fold_dir_prefix, 'imagesTr')
    only_files = [f for f in listdir(src_dir) if isfile(join(src_dir, f))]
    for f in only_files:
        if is_modality_file_func(f):
            shutil.copy(join(src_dir, f), images_tr_folder)
    if is_t2_only:
        rename_t2_files(images_tr_folder)
