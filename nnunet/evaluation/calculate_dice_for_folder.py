import sys
from os import listdir
from os.path import isfile, join
from calculate_dice import calculate_dice_coefficient


def main(inferred_fldr, gt_folder):
    inferred_files = [f for f in listdir(inferred_fldr) if isfile(join(inferred_fldr, f))]
    file_count = 0
    total = 0.0
    for inferred_file in inferred_files:
        if inferred_file.endswith('pkl'):
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
    inferred_folder = sys.argv[1]
    ground_truth_folder = sys.argv[2]
    main(inferred_folder, ground_truth_folder)
