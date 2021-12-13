import os
from os import listdir
from os.path import isfile, join
from os.path import exists

images_tr_source = \
    '/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task517_Paper_Fold1/imagesTr/'
images_tr_destination = \
    '/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task519_Paper_Fold3/imagesTr/'

images_tr_file = [f for f in listdir(images_tr_source) if
                  isfile(join(images_tr_source, f)) and f.startswith('SynthSeg')]
for file in images_tr_file:
    src_file = os.path.join(images_tr_source, file)
    dest_file = os.path.join(images_tr_destination, file)
    file_exists = exists(dest_file)
    if not file_exists:
        cmd = 'ln -s {} {}'.format(src_file, dest_file)
        returned_value = os.system(cmd)
        if returned_value != 0:
            print('returned value:', returned_value)

labels_tr_source = \
    '/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task517_Paper_Fold1/labelsTr/'
labels_tr_destination = \
    '/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task519_Paper_Fold3/labelsTr/'

labels_tr_files = \
    [f for f in listdir(labels_tr_source) if isfile(join(labels_tr_source, f)) and f.startswith('SynthSeg')]
for file in labels_tr_files:
    src_file = os.path.join(labels_tr_source, file)
    dest_file = os.path.join(labels_tr_destination, file)
    file_exists = exists(dest_file)
    if not file_exists:
        cmd = 'ln -s {} {}'.format(src_file, dest_file)
        returned_value = os.system(cmd)
        if returned_value != 0:
            print('returned value:', returned_value)
