from os import listdir
from os.path import isfile, join
from shutil import copyfile

images_tr_dir = '/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task504_AllAgesWithSkull' \
                '/imagesTr/'
labels_tr_dir = '/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task504_AllAgesWithSkull' \
                '/labelsTr/'
wm_jlf_atlases_dir = '/home/feczk001/shared/data/nnUNet/JLF_templates_testing/wm_JLF_atlases/'
onlyfiles = [f for f in listdir(images_tr_dir) if isfile(join(images_tr_dir, f))]
for file in onlyfiles:
    if '0001' in file:
        continue
    months = file[:3]
    template = file[4:14]
    identifier = file[:-7]
    print(file)
    src = join(wm_jlf_atlases_dir, months, template, 'Segmentation.nii.gz')
    dst = join(labels_tr_dir, identifier[:-5] + '.nii.gz')
    copyfile(src, dst)
