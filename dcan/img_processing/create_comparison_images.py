# Author: Paul Reiners

import sys
from os import listdir
from os.path import isfile, join
import os
from pathlib import Path

from dcan.img_processing.create_segmentation_images import create_segmentation_images


def create_comparison_images(inferred_fldr, gt_folder, output_dir):
    inferred_files = [f for f in listdir(inferred_fldr) if isfile(join(inferred_fldr, f))]
    for inferred_file in inferred_files:
        if inferred_file.endswith('pkl') or inferred_file.endswith('json'):
            continue
        inferred_file_path = join(inferred_fldr, inferred_file)
        print("inferred_file:", inferred_file)
        gt_file_path = join(gt_folder, inferred_file)
        base_name = inferred_file[:-7]
        ground_truth_folder = os.path.join(output_dir, base_name, "ground_truth")
        Path(ground_truth_folder).mkdir(parents=True, exist_ok=True)
        create_segmentation_images(gt_file_path, ground_truth_folder)
        inferred_folder = os.path.join(output_dir, base_name, "inferred")
        Path(inferred_folder).mkdir(parents=True, exist_ok=True)
        create_segmentation_images(inferred_file_path, inferred_folder)


if __name__ == "__main__":
    inferred_folder = sys.argv[1]
    ground_truth_folder = sys.argv[2]
    output_dir = sys.argv[3]
    create_comparison_images(inferred_folder, ground_truth_folder, output_dir)
