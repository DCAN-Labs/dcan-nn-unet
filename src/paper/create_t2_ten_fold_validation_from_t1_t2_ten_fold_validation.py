import argparse
import sys

from paper.create_single_contrast_ten_fold_validation_from_t1_t2_ten_fold_validation import \
    create_single_contrast_ten_fold_validation_from_t1_t2_ten_fold_validation
from paper.create_t1_ten_fold_validation_from_t1_t2_ten_fold_validation import get_args


def main() -> int:
    """Create T1-only 10-fold validation folders from T1/T2 10-fold validation folders."""
    parser = argparse.ArgumentParser(
        prog='create_t2_ten_fold_validation_from_t1_t2_ten_fold_validation',
        description='Create stratified 10-fold validation folders of T2 images from T1/T2 images.',
        epilog='Contact reine097 if you have any questions or run into any problems.')
    first_destination_task_number, first_source_task_number, parent_destination_folder, parent_source_folder = get_args(
        parser)
    create_single_contrast_ten_fold_validation_from_t1_t2_ten_fold_validation(
        parent_source_folder, first_source_task_number, parent_destination_folder, first_destination_task_number,
        '0001', 'T2')

    return 0


if __name__ == '__main__':
    sys.exit(main())
