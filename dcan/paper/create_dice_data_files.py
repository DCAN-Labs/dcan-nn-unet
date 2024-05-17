import os
import sys
import nibabel as nib
import pickle
from tqdm import tqdm

from evaluation.calculate_dice_for_region import calculate_dice_coefficient

STEP = 4


def main(ground_truth_folder, inferred_files_folder, output_pickle_file, step=1):
    free_surfer_lut_dcan_file = open('../../doc/Freesurfer_LUT_DCAN.txt', 'r')
    lines_of_text = free_surfer_lut_dcan_file.readlines()
    d = dict()
    region_numbers = []
    for line_of_text in tqdm(lines_of_text):
        line_of_text = line_of_text.strip()
        if line_of_text.startswith('#') or not line_of_text:
            continue
        parts = line_of_text.split()
        region_number = int(parts[0])
        region_numbers.append(region_number)

    for region_number in region_numbers:
        if region_number not in d:
            d[region_number] = []
        for ground_truth_path in tqdm(os.listdir(ground_truth_folder), leave=False):
            if os.path.isfile(os.path.join(ground_truth_folder, ground_truth_path)):
                inferred_file = os.path.join(inferred_files_folder, ground_truth_path)
                file_ts_img = nib.load(inferred_file)
                file_ts_img.get_fdata()
                gt_label_file = os.path.join(ground_truth_folder, ground_truth_path)
                dice_coefficient = calculate_dice_coefficient(gt_label_file, inferred_file, region_number, step)
                d[region_number].append(dice_coefficient)

    dbfile = open(output_pickle_file, 'wb')
    pickle.dump(d, dbfile)
    dbfile.close()


if __name__ == '__main__':
    gt_folder = sys.argv[1]
    inferred_files = sys.argv[2]
    output_pickle_file = sys.argv[3]
    main(gt_folder, inferred_files, STEP)
