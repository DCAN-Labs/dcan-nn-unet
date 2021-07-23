import os
from os.path import isfile, join
from os import listdir
from shutil import copyfile


src_dir = '/home/feczk001/shared/data/nnUNet/JLF_templates_testing/wm_JLF_atlases/head_files'
dest_dir = '/home/feczk001/shared/data/nnUNet/JLF_templates_testing/wm_JLF_atlases/head_files_flattened/'

subfolders = next(os.walk(src_dir))[1]
for subfolder in subfolders:
    subfolder_path = os.path.join(src_dir, subfolder)
    onlyfiles = [f for f in listdir(subfolder_path) if isfile(join(subfolder_path, f))]
    for file in onlyfiles:
        if 'T1' in file:
            suffix = '_0000'
        else:
            suffix = '_0001'
        new_file_name = subfolder + '_' + file[:-7] + suffix + ".nii.gz"
        src = join(subfolder_path, file)
        dst = join(dest_dir, new_file_name)
        copyfile(src, dst)

