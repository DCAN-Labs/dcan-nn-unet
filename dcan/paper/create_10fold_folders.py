import sys
import os.path
from os import listdir
from os.path import isfile, join
from shutil import copy
import argparse
from argparse import RawTextHelpFormatter

def create_folders():
    for i in range(1, 11): # Create fold folder
        if not os.path.exists(f'Fold_{i}'):
            os.mkdir(f'Fold_{i}')
            for j in ["Test", "Train"]: # Test and Train folders
                for x in ["Images", "Segmentations"]: # Image and Segmentation folders
                    if not os.path.exists(os.path.join(f'Fold_{i}', j, x)):
                        os.makedirs(os.path.join(f'Fold_{i}', j, x))

def populate_folders(test_segmentations, test_images, model_type):
    segmentations = os.listdir(test_segmentations)
    images = os.listdir(test_images)

    for fold_num in range(10): # loop through each of the 10 fold folders
        # SEGMENTATIONS
        for seg_file_index in range(len(segmentations)): # evenly and uniquely populate train and test data by age
            if seg_file_index % 10 == fold_num: # Test data
                if not os.path.exists(os.path.join(f'Fold_{fold_num + 1}', "Test", "Segmentations", segmentations[seg_file_index])):
                    copy(os.path.join(test_segmentations, segmentations[seg_file_index]), os.path.join(f'Fold_{fold_num + 1}', "Test", "Segmentations"))
            else:   # Train data
                if not os.path.exists(os.path.join(f'Fold_{fold_num + 1}', "Train", "Segmentations", segmentations[seg_file_index])):
                    copy(os.path.join(test_segmentations, segmentations[seg_file_index]), os.path.join(f'Fold_{fold_num + 1}', "Train", "Segmentations"))   

        #IMAGES
        for img_file_index in range(len(images)): # evenly and uniquely populate train and test data by age
            if img_file_index % 10 == (fold_num * 2): # Test data
                if (model_type == 0 or model_type == 2) and (not os.path.exists(os.path.join(f'Fold_{fold_num + 1}', "Test", "Images", images[img_file_index]))):
                    copy(os.path.join(test_images, images[img_file_index]), os.path.join(f'Fold_{fold_num + 1}', "Test", "Images"))
                if (model_type == 1 or model_type == 2) and (not os.path.exists(os.path.join(f'Fold_{fold_num + 1}', "Test", "Images", images[img_file_index + 1]))):
                    copy(os.path.join(test_images, images[img_file_index + 1]), os.path.join(f'Fold_{fold_num + 1}', "Test", "Images"))
            else: # Train data
                if (model_type == 0 or model_type == 2) and (not os.path.exists(os.path.join(f'Fold_{fold_num + 1}', "Train", "Images", images[img_file_index]))):
                    copy(os.path.join(test_images, images[img_file_index]), os.path.join(f'Fold_{fold_num + 1}', "Train", "Images"))
                if (model_type == 1 or model_type == 2) and (not os.path.exists(os.path.join(f'Fold_{fold_num + 1}', "Train", "Images", images[img_file_index + 1]))):
                    copy(os.path.join(test_images, images[img_file_index + 1]), os.path.join(f'Fold_{fold_num + 1}', "Train", "Images"))
def main():
    parser = argparse.ArgumentParser(
        description='Create and populate 10-fold cross validation folders',
        formatter_class=RawTextHelpFormatter
    )
    parser.add_argument("--seg-folder", required=True, help="Path to segmentation files")
    parser.add_argument("--img-folder", required=True, help="Path to image files")
    parser.add_argument("--model-type", type=int, choices=[0, 1, 2], default=2,
                       help="Model type: 0 for t1 only, 1 for t2 only, 2 for both")
    args = parser.parse_args()

    create_folders()
    populate_folders(args.seg_folder, args.img_folder, args.model_type)

if __name__ == "__main__":
    main()