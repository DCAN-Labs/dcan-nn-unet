"""Usage: calculate_dice_for_folder <inferred_folder> <ground_truth_folder>"""
from docopt import docopt

# Author: Paul Reiners

import sys
from os import listdir
from os.path import isfile, join
from calculate_dice import calculate_dice_coefficient


def calculate_dice_for_folder(inferred_fldr, gt_folder):
    inferred_files = [f for f in listdir(inferred_fldr) if isfile(join(inferred_fldr, f))]
    file_count = 0
    total = 0.0
    for inferred_file in inferred_files:
        if inferred_file.endswith('pkl') or inferred_file.endswith('json'):
            continue
        file_count += 1
        inferred_file_path = join(inferred_fldr, inferred_file)
        print("inferred_file:", inferred_file)
        gt_file_path = join(gt_folder, inferred_file)
        dice_coefficient = calculate_dice_coefficient(gt_file_path, inferred_file_path)
        total += dice_coefficient
        print('dice (foreground):', dice_coefficient)
    print('\navg dice:', total / file_count)


if __name__ == "__main__":
    arguments = docopt(__doc__)
    calculate_dice_for_folder(arguments['<inferred_folder>'], arguments['<ground_truth_folder>'])
