import os
import shutil

base_dir_1 = '/scratch.global/hendr522-BIBSNet-T2only/nnUNet_raw_data/'
base_dir_2 = '/scratch.global/lundq163/nnUNet/BOBSnet_raw_data_base/nnUNet_raw_data/'

result = \
    [[dp, f] for dp, dn, filenames in os.walk(base_dir_2) for f in filenames
     if (not f.endswith('_0000.nii.gz') and not f == 'dataset.json')]
for f in result:
    directory = f[0]
    dir_extension = directory[len(base_dir_2):]
    other_dir_extension = dir_extension.replace('70', '72', 1)
    f1 = f[1]
    other_f1 = f1.replace('_0001.nii.gz', '_0000.nii.gz')
    other_file_path = os.path.join(base_dir_1, other_dir_extension, other_f1)
    if not os.path.isfile(other_file_path):
        shutil.copyfile(os.path.join(directory, f1), other_file_path)
