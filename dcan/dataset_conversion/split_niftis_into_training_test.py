from os import listdir, mkdir
from os.path import isfile, join
import random
import shutil


def copy_files(files, origin_labels_folder, destination_labels_folder, origin_images_folder, destination_images_folder):
    for file in files:
        shutil.copyfile(origin_labels_folder + '/' + file, destination_labels_folder + '/' + file)
        base_file = file[:-7]
        t1_image_file = base_file + '_0000.nii.gz'
        shutil.copyfile(origin_images_folder + '/' + t1_image_file, destination_images_folder + '/' + t1_image_file)
        t2_image_file = base_file + '_0001.nii.gz'
        shutil.copyfile(origin_images_folder + '/' + t2_image_file, destination_images_folder + '/' + t2_image_file)


def main():
    origin_folder = '/home/miran045/reine097/JLF_templates_testing/flat_wm_JLF_atlases/'
    labels_folder = origin_folder + 'labels'
    images_folder = origin_folder + 'images'
    destination_folder = '/home/miran045/reine097/nnUNet_raw_data_base/nnUNet_raw_data/Task002_Babies/'
    images_tr_folder = destination_folder + 'imagesTr'
    mkdir(images_tr_folder)
    images_ts_folder = destination_folder + 'imagesTs'
    mkdir(images_ts_folder)
    labels_tr_folder = destination_folder + 'labelsTr'
    mkdir(labels_tr_folder)
    labels_ts_folder = destination_folder + 'labelsTs'
    mkdir(labels_ts_folder)

    label_files = [f for f in listdir(labels_folder) if isfile(join(labels_folder, f))]

    random.shuffle(label_files)
    n = len(label_files)
    train_count = (7 * n) // 10
    train_data = label_files[:train_count]
    copy_files(train_data, labels_folder, labels_tr_folder, images_folder, images_tr_folder)

    test_data = label_files[train_count:]
    copy_files(test_data, labels_folder, labels_ts_folder, images_folder, images_ts_folder)


if __name__ == "__main__":
    main()
