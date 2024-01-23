import argparse
import os
import os.path
import sys

from paper.create_single_contrast_ten_fold_validation_from_t1_t2_ten_fold_validation import \
    create_single_contrast_ten_fold_validation_from_t1_t2_ten_fold_validation


def main() -> int:
    """Create T1-only 10-fold validation folders from T1/T2 10-fold validation folders."""
    parser = argparse.ArgumentParser(
        prog='create_t1_ten_fold_validation_from_t1_t2_ten_fold_validation',
        description='Create stratified 10-fold validation folders of T1 images from T1/T2 images.',
        epilog='Contact reine097 if you have any questions or run into any problems.')
    first_destination_task_number, first_source_task_number, parent_destination_folder, parent_source_folder = get_args(
        parser)
    create_single_contrast_ten_fold_validation_from_t1_t2_ten_fold_validation(
        parent_source_folder, first_source_task_number, parent_destination_folder, first_destination_task_number,
        '0000', 'T1')

    return 0


def get_args(parser):
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
    return first_destination_task_number, first_source_task_number, parent_destination_folder, parent_source_folder


if __name__ == '__main__':
    sys.exit(main())
