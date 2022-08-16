from os import path
from os import listdir
from os.path import isfile, join
import shutil


def copy_files(data_folder, folder_name, src_folder):
    dest_folder = path.join(data_folder, f'Task526_Paper_All/{folder_name}')
    dest_files = [f for f in listdir(dest_folder) if isfile(join(dest_folder, f))]
    src_files = [f for f in listdir(path.join(data_folder, src_folder)) if isfile(join(src_folder, f))]
    for f in src_files:
        if f not in dest_files:
            shutil.copyfile(path.join(src_folder, f), path.join(dest_folder, f))


task_nums = range(516, 526)
index = 0
raw_data_folder = '/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data'
for task_num in task_nums:
    # imagesTr
    src_images_Tr_folder = join(raw_data_folder, f'Task{task_num}_Paper_Fold{index}/imagesTr')
    copy_files(raw_data_folder, 'imagesTr', src_images_Tr_folder)

    # labelsTr
    src_labels_Tr_folder = path.join(raw_data_folder, f'Task{task_num}_Paper_Fold{index}/labelsTr')
    copy_files(raw_data_folder, 'labelsTr', src_labels_Tr_folder)

    index += 1
