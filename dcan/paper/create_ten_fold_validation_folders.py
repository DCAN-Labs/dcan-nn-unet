import os.path
from os import listdir
from os.path import isfile, join
from shutil import copyfile

from sklearn.model_selection import StratifiedKFold

nnunet_raw_data_folder = '/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data'
folder_512 = '/home/feczk001/shared/data/nnUNet/raw_data/Task512/'
all_images = [f for f in listdir(folder_512) if isfile(join(folder_512, f))]
all_images.sort()
all_images = all_images[::3]
all_images = list(set([f[:-7] for f in all_images]))
classes = [int(f[0]) for f in all_images]
skf = StratifiedKFold(n_splits=10)
task_number = 516
fold = 0
for train, test in skf.split(all_images, classes):
    task_name = 'Task{}_Paper_Fold{}'.format(task_number, fold)
    task_folder_name = os.path.join(nnunet_raw_data_folder, task_name)
    if not os.path.exists(task_folder_name):
        os.mkdir(task_folder_name)
    dest_images_tr_folder = os.path.join(task_folder_name, "imagesTr")
    if not os.path.exists(dest_images_tr_folder):
        os.mkdir(dest_images_tr_folder)
    dest_images_ts_folder = os.path.join(task_folder_name, "imagesTs")
    if not os.path.exists(dest_images_ts_folder):
        os.mkdir(dest_images_ts_folder)
    dest_labels_tr_folder = os.path.join(task_folder_name, "labelsTr")
    if not os.path.exists(dest_labels_tr_folder):
        os.mkdir(dest_labels_tr_folder)
    for i in train:
        base_file_name = all_images[i]
        t1_src_file = base_file_name + '_0000.nii.gz'
        copyfile(os.path.join(folder_512, t1_src_file), os.path.join(dest_images_tr_folder, t1_src_file))
        t2_src_file = base_file_name + '_0001.nii.gz'
        copyfile(os.path.join(folder_512, t2_src_file), os.path.join(dest_images_tr_folder, t2_src_file))
        label_src_file = base_file_name + '.nii.gz'
        copyfile(os.path.join(folder_512, label_src_file), os.path.join(dest_labels_tr_folder, label_src_file))
    for i in test:
        base_file_name = all_images[i]
        t1_src_file = base_file_name + '_0000.nii.gz'
        copyfile(os.path.join(folder_512, t1_src_file), os.path.join(dest_images_ts_folder, t1_src_file))
        t2_src_file = base_file_name + '_0001.nii.gz'
        copyfile(os.path.join(folder_512, t2_src_file), os.path.join(dest_images_ts_folder, t2_src_file))
    task_number += 1
    fold += 1
