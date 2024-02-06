# Author: Paul Reiners

from os import listdir
from os.path import isfile, join
import os

my_path = '/home/feczk001/shared/projects/nnunet_predict/nnunet_echo_input/to_run_resized/'
only_files = [f for f in listdir(my_path) if isfile(join(my_path, f))]
for file in only_files:
    modality = (file[-11:-7])
    if modality == '0000':
        matching_pair_modality = '0001'
    else:
        matching_pair_modality = '0000'
    matching_file = file[:-11] + matching_pair_modality + '.nii.gz'
    if matching_file not in only_files:
        print("Found file without a match:", file)
        os.remove(os.path.join(my_path, file))
