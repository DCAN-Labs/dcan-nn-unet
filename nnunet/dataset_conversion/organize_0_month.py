from os import listdir
from os.path import isfile, join
from shutil import copyfile

ASEG = 'aseg_'
T1W = "T1w_"
T2W = "T2w_"
file_extension = ".nii.gz"

root_dir = '/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task509/0mo/'
dest_dir = '/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task509/flat/'

onlyfiles = [f for f in listdir(root_dir) if isfile(join(root_dir, f))]
for f in onlyfiles:
    index = f[-9:-7]
    aseg_len = len(ASEG)
    new_name = ''
    if f.startswith(ASEG):
        new_name = '0mo_{}'.format(f[aseg_len:])
    elif f.startswith(T1W):
        new_name = '0mo_{}_0000.nii.gz'.format(f[len(T1W):-len(file_extension)])
    elif f.startswith(T2W):
        new_name = '0mo_{}_0001.nii.gz'.format(f[len(T2W):-len(file_extension)])
    else:
        assert (False, "Unexpected file name")
    print(new_name)
    copyfile(join(root_dir, f), join(dest_dir, new_name))
