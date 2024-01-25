import glob
import os
import shutil
from pathlib import Path

from tqdm.contrib import itertools
from typing import Tuple


def create_single_contrast_ten_fold_validation_from_t1_t2_ten_fold_validation(
        parent_source_folder: str, first_source_task_number: int, parent_destination_folder: str,
        first_destination_task_number: int, contrast_code: str, contrast_name: str) -> None:
    """
    Creates ten-fold validation folders for a single contrast type.

    Args:
        parent_source_folder (str): The T1/T2 folder from which the single contrast folder is being created.
        first_source_task_number (int): The starting nnU-Net task number.
        parent_destination_folder (str): The folder where the single contrast folders will go.
        first_destination_task_number: (int) The starting task number for the single contrast folds.
        contrast_code (str): The code that is appended to the anatomical images, such as '0000'.
        contrast_name (str): The abbreviation of the contrast, such as 'T1'.

    Returns:
        None.
    """
    images_folders = ['imagesTr', 'imagesTs']
    labels_folders = ['labelsTr', 'labelsTs']
    folders = images_folders + labels_folders
    for i, folder in itertools.product(range(10), folders):
        if folder.startswith('images'):
            source_folder, destination_folder = \
                get_folders(first_destination_task_number, first_source_task_number, folder, i,
                            parent_destination_folder, parent_source_folder, contrast_name)
            for file_to_copy in glob.glob(os.path.join(source_folder, f'*_{contrast_code}.nii.gz')):
                shutil.copy(file_to_copy, destination_folder)
        elif folder.startswith('labels'):
            source_folder, destination_folder = \
                get_folders(
                    first_destination_task_number, first_source_task_number, folder, i, parent_destination_folder,
                    parent_source_folder, contrast_name)
            for file_to_copy in glob.glob(os.path.join(source_folder, '*.nii.gz')):
                shutil.copy(file_to_copy, destination_folder)
        else:
            assert False


def get_folders(first_destination_task_number: int, first_source_task_number: int, folder: str, i: int,
                parent_destination_folder: str, parent_source_folder: str, contrast_name: str) -> Tuple[str, str]:
    source_folder = \
        os.path.join(
            parent_source_folder, f'Task{str(first_source_task_number + i)}_T1_T2_Fold{str(i)}', folder)
    destination_folder = \
        os.path.join(
            parent_destination_folder, f'Task{str(first_destination_task_number + i)}_{contrast_name}_Fold{str(i)}',
            folder)
    Path(destination_folder).mkdir(parents=True, exist_ok=True)

    return source_folder, destination_folder
