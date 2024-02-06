import os
import shutil
import sys
from os import listdir, mkdir
from os.path import isfile, join

import glob

from sklearn.model_selection import train_test_split
from tqdm import tqdm


def copy_files(files, origin_labels_folder, destination_labels_folder, origin_images_folder, destination_images_folder):
    for file in tqdm(files):
        shutil.copyfile(origin_labels_folder + '/' + file, destination_labels_folder + '/' + file)
        base_file = file[:-7]
        t1_image_file = base_file + '_0000.nii.gz'
        shutil.copyfile(origin_images_folder + '/' + t1_image_file, destination_images_folder + '/' + t1_image_file)
        t2_image_file = base_file + '_0001.nii.gz'
        shutil.copyfile(origin_images_folder + '/' + t2_image_file, destination_images_folder + '/' + t2_image_file)


def main(origin_folder, destination_folder):
    labels_folder = os.path.join(origin_folder, 'labels')
    images_folder = os.path.join(origin_folder, 'images')
    images_tr_folder = os.path.join(destination_folder, 'imagesTr')
    if not os.path.exists(images_tr_folder):
        mkdir(images_tr_folder)
    images_ts_folder = os.path.join(destination_folder, 'imagesTs')
    if not os.path.exists(images_ts_folder):
        mkdir(images_ts_folder)
    labels_tr_folder = os.path.join(destination_folder, 'labelsTr')
    if not os.path.exists(labels_tr_folder):
        mkdir(labels_tr_folder)
    labels_ts_folder = os.path.join(destination_folder, 'labelsTs')
    if not os.path.exists(labels_ts_folder):
        mkdir(labels_ts_folder)

    synthseg_images_file_list = glob.glob('./images/*SynthSeg_generated*.nii.gz')
    for synthseg_image_file in tqdm(synthseg_images_file_list):
        basename = os.path.basename(synthseg_image_file)
        shutil.move(f"./images/{basename}", f"./imagesTr/{basename}")

    synthseg_labels_file_list = glob.glob('./labels/*SynthSeg_generated*.nii.gz')
    for synthseg_label_file in tqdm(synthseg_labels_file_list):
        basename = os.path.basename(synthseg_label_file)
        shutil.move(f"./labels/{basename}", f"./labelsTr/{basename}")

    label_files = [f for f in listdir(labels_folder) if isfile(join(labels_folder, f))]
    label_files.sort()
    image_files = [f for f in listdir(images_folder) if isfile(join(images_folder, f))]
    image_files.sort()
    image_file_pairs = [(image_files[2 * i], image_files[2 * i + 1]) for i in range(len(label_files))]

    stratify = [int(label_file[0]) for label_file in label_files]
    _, _, train_data, test_data = train_test_split(image_file_pairs, label_files, test_size=0.33, random_state=42,
                                                   stratify=stratify)
    copy_files(train_data, labels_folder, labels_tr_folder, images_folder, images_tr_folder)
    copy_files(test_data, labels_folder, labels_ts_folder, images_folder, images_ts_folder)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
