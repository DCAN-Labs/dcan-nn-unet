"""Usage: calculate_dice_for_folder <ground_truth_folder> <inferred_folder>"""
from os import listdir
from os.path import isfile, join, exists

from docopt import docopt


# Author: Paul Reiners
from dcan.evaluation.calculate_dice import calculate_dice_coefficient


def calculate_dice_for_folder(gt_folder, inferred_fldr):
    if not exists(gt_folder) or not exists(inferred_fldr):
        return {}
    inferred_files = [f for f in listdir(inferred_fldr) if isfile(join(inferred_fldr, f))]
    file_count = 0
    total = 0.0
    results = {}
    file_results = {}
    for inferred_file in inferred_files:
        if inferred_file.endswith('pkl') or inferred_file.endswith('json'):
            continue
        file_count += 1
        inferred_file_path = join(inferred_fldr, inferred_file)
        gt_file_path = join(gt_folder, inferred_file)
        dice_coefficient = calculate_dice_coefficient(gt_file_path, inferred_file_path)
        total += dice_coefficient
        file_results[inferred_file] = dice_coefficient
    results['file_results'] = file_results
    avg_dice = total / file_count
    results['avg_dice'] = avg_dice

    return results


if __name__ == "__main__":
    arguments = docopt(__doc__)
    calculate_dice_for_folder(arguments['<ground_truth_folder>'], arguments['<inferred_folder>'])
