import argparse
import glob
import os.path
import sys
from pathlib import Path
import os

from tqdm.contrib import itertools
import shutil


def create_t1_ten_fold_validation_from_t1_t2_ten_fold_validation(
        parent_source_folder, first_source_task_number, parent_destination_folder, first_destination_task_number):
    images_folders = ['imagesTr', 'imagesTs']
    labels_folders = ['labelsTr', 'labelsTs']
    folders = images_folders + labels_folders
    for i, folder in itertools.product(range(10), folders):
        if folder.startswith('images'):
            source_folder, destination_folder = \
                get_folders(first_destination_task_number, first_source_task_number, folder, i,
                            parent_destination_folder, parent_source_folder)
            for file_to_copy in glob.glob(os.path.join(source_folder, '*_0000.nii.gz')):
                shutil.copy(file_to_copy, destination_folder)
        elif folder.startswith('labels'):
            source_folder, destination_folder = \
                get_folders(
                    first_destination_task_number, first_source_task_number, folder, i, parent_destination_folder,
                    parent_source_folder)
            for file_to_copy in glob.glob(os.path.join(source_folder, '*.nii.gz')):
                shutil.copy(file_to_copy, destination_folder)
        else:
            assert False


def get_folders(first_destination_task_number, first_source_task_number, folder, i, parent_destination_folder,
                parent_source_folder):
    source_folder = \
        os.path.join(
            parent_source_folder, f'Task{str(first_source_task_number + i)}_T1_T2_Fold{str(i)}', folder)
    destination_folder = \
        os.path.join(
            parent_destination_folder, f'Task{str(first_destination_task_number + i)}_T1_Fold{str(i)}',
            folder)
    Path(destination_folder).mkdir(parents=True, exist_ok=True)

    return source_folder, destination_folder


def main() -> int:
    """Create T1-only 10-fold validation folders from T1/T2 10-fold validation folders."""
    parser = argparse.ArgumentParser(
        prog='create_t1_ten_fold_validation_from_t1_t2_ten_fold_validation',
        description='Create stratified 10-fold validation folders of T1 images from T1/T2 images.',
        epilog='Contact reine097 if you have any questions or run into any problems.')
    parser.add_argument('parent_source_folder')
    parser.add_argument('first_source_task_number')
    parser.add_argument('parent_destination_folder')
    parser.add_argument('first_destination_task_number')
    args = parser.parse_args()
    parent_source_folder = args.parent_source_folder
    if not os.path.isdir(parent_source_folder):
        print(f'Parent source folder does not exist: {parent_source_folder}')
    first_source_task_number = int(args.first_source_task_number)
    parent_destination_folder = args.parent_destination_folder
    if not os.path.isdir(parent_destination_folder):
        print(f'Parent destination folder does not exist: {parent_destination_folder}')
    first_destination_task_number = int(args.first_destination_task_number)
    create_t1_ten_fold_validation_from_t1_t2_ten_fold_validation(
        parent_source_folder, first_source_task_number, parent_destination_folder, first_destination_task_number)

    return 0


if __name__ == '__main__':
    sys.exit(main())
