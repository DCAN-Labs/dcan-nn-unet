import os
from shutil import copyfile


source_directory = '/home/feczk001/shared/data/nnUNet/lab2im_generated_images/Task510/'
images_tr_directory = \
    ('/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task510_BCP_ABCD_Neonates_Augmentation/'
     'imagesTr/')
labels_tr_directory = \
    ('/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task510_BCP_ABCD_Neonates_Augmentation/'
     'labelsTr/')

files = os.listdir(source_directory)

for f in files:
    print(f)
    if f.endswith('_0000.nii.gz') or f.endswith('_0001.nii.gz'):
        dst = images_tr_directory
    else:
        dst = labels_tr_directory
    src = os.path.join(source_directory, f)
    dst_path = os.path.join(dst, f)
    copyfile(src, dst_path)
