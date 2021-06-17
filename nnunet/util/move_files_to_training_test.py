from os import listdir
from os.path import isfile, join
import random
import shutil

src_folder = '/home/miran045/reine097/JLF_templates_testing/flat_wm_JLF_atlases/'
labels_folder = src_folder + 'labels'
only_files = [f for f in listdir(labels_folder) if isfile(join(labels_folder, f))]
names = [s[:-7] for s in only_files]
n = len(names)
train_count = round(n * 0.8)
training_names = random.sample(names, train_count)
test_names = [n for n in names if n not in training_names]
images_src_folder = src_folder + 'images/'
labels_src_folder = src_folder + 'labels/'
destination_folder = '/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task501_Babies_AllMonths/'
labels_tr_folder = destination_folder + 'labelsTr'
image_type_count = 3
images_tr_folder = destination_folder + 'imagesTr'
for training_name in training_names:
    for i in range(image_type_count):
        image_source_file_path = '{}{}_000{}.nii.gz'.format(images_src_folder, training_name, str(i))
        shutil.copy(image_source_file_path, images_tr_folder)
    label_source_file_path = '{}{}.nii.gz'.format(labels_src_folder, training_name)
    shutil.copy(label_source_file_path, labels_tr_folder)
images_ts_folder = destination_folder + 'imagesTs'
for test_name in test_names:
    for i in range(image_type_count):
        image_source_file_path = '{}{}_000{}.nii.gz'.format(images_src_folder, test_name, str(i))
        shutil.copy(image_source_file_path, images_ts_folder)
