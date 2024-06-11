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
        for img_file_index in range(0, len(images), 2): # evenly and uniquely populate train and test data by age
            if img_file_index % 20 == (fold_num * 2): # Test data
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

    #parser = argparse.ArgumentParser(description='Do stuff')
    #parser.add_argument("dest_folder", help="output folder")
    #args = parser.parse_args()
    #print(args.echo)

    test_segmentations = '/scratch.global/lundq163/E_and_K_test_segs/'
    test_images = '/scratch.global/lundq163/E_and_K_test_imgs/'

    # 0: t1 only, 1: t2 only, 2: both
    model_type = 2

    create_folders()
    populate_folders(test_segmentations, test_images, model_type)

if __name__ == "__main__":
    main()