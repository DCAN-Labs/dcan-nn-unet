import sys
import os.path
from os import listdir
from os.path import isfile, join
from shutil import copy
import argparse
from argparse import RawTextHelpFormatter

def create_folders(num_folds):
    for i in range(1, num_folds + 1): # Create fold folder
        if not os.path.exists(f'Fold_{i}'):
            os.mkdir(f'Fold_{i}')
            for j in ["Test", "Train"]: # Test and Train folders
                for x in ["Images", "Segmentations"]: # Image and Segmentation folders
                    if not os.path.exists(os.path.join(f'Fold_{i}', j, x)):
                        os.makedirs(os.path.join(f'Fold_{i}', j, x))

def populate_folders(test_segmentations, test_images, model_type, num_folds, split_ratio):
    segmentations = os.listdir(test_segmentations)
    images = os.listdir(test_images)
    if split_ratio == 0.1:
        test_index = 10
    elif split_ratio == 0.2:
        test_index = 5

    for fold_num in range(num_folds): # loop through each of the 10 fold folders
        # SEGMENTATIONS
        for seg_file_index in range(len(segmentations)): # evenly and uniquely populate train and test data by age
            if seg_file_index % test_index == 0: # Test data
                if not os.path.exists(os.path.join(f'Fold_{fold_num + 1}', "Test", "Segmentations", segmentations[seg_file_index])):
                    copy(os.path.join(test_segmentations, segmentations[seg_file_index]), os.path.join(f'Fold_{fold_num + 1}', "Test", "Segmentations"))
            else:   # Train data
                if not os.path.exists(os.path.join(f'Fold_{fold_num + 1}', "Train", "Segmentations", segmentations[seg_file_index])):
                    copy(os.path.join(test_segmentations, segmentations[seg_file_index]), os.path.join(f'Fold_{fold_num + 1}', "Train", "Segmentations"))
                    
        if model_type == 0:
            test_index = 2 * test_index

        #IMAGES
        for img_file_index in range(len(images)): # evenly and uniquely populate train and test data by age
            if model_type == 0: # Both T1 and T2
                if img_file_index % test_index == 0 or img_file_index % test_index == 1: # Test data
                    if not os.path.exists(os.path.join(f'Fold_{fold_num + 1}', "Test", "Images", images[img_file_index])):
                        copy(os.path.join(test_images, images[img_file_index]), os.path.join(f'Fold_{fold_num + 1}', "Test", "Images"))
                else:   # Train data
                    if not os.path.exists(os.path.join(f'Fold_{fold_num + 1}', "Train", "Images", images[img_file_index])):
                        copy(os.path.join(test_images, images[img_file_index]), os.path.join(f'Fold_{fold_num + 1}', "Train", "Images")) 
            else:
                if img_file_index % test_index == 0: # Test data
                    if not os.path.exists(os.path.join(f'Fold_{fold_num + 1}', "Test", "Images", images[img_file_index])):
                        copy(os.path.join(test_images, images[img_file_index]), os.path.join(f'Fold_{fold_num + 1}', "Test", "Images"))
                else:   # Train data
                    if not os.path.exists(os.path.join(f'Fold_{fold_num + 1}', "Train", "Images", images[img_file_index])):
                        copy(os.path.join(test_images, images[img_file_index]), os.path.join(f'Fold_{fold_num + 1}', "Train", "Images"))

def main():
    parser = argparse.ArgumentParser(
        description='Create and populate 10-fold cross validation folders',
        formatter_class=RawTextHelpFormatter
    )
    parser.add_argument("--seg-folder", required=True, help="Path to segmentation files")
    parser.add_argument("--img-folder", required=True, help="Path to image files")
    parser.add_argument("--model-type", type=int, choices=[0, 1, 2], default=0,
                       help="Model type: 1 for t1 only, 2 for t2 only, 0 for both")
    parser.add_argument("--num-folds", type=int, default=10, help="Number of folds for cross-validation (default: 10)")
    parser.add_argument("--split-ratio", type=float, choices=[0.1, 0.2], default=0.2, help="Split between train and test data (choices: 0.1 or 0.2, default: 0.2)")
    args = parser.parse_args()

    create_folders(args.num_folds)
    populate_folders(args.seg_folder, args.img_folder, args.model_type, args.num_folds, args.split_ratio)
if __name__ == "__main__":
    main()