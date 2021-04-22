import os
from shutil import copyfile


origin_dir = '/home/miran045/reine097/JLF_templates_testing/wm_JLF_atlases'
destination_dir = '/home/miran045/reine097/JLF_templates_testing/flat_wm_JLF_atlases/'

for sub_folder in os.listdir(origin_dir):
    for template_folder in os.listdir(origin_dir + '/' + sub_folder):
        current_folder = origin_dir + '/' + sub_folder + '/' + template_folder
        segmentation_file = current_folder + '/Segmentation.nii.gz'
        destination_segmentation_file = \
            "{}/labels/{}_{}.nii.gz".format(destination_dir, sub_folder, template_folder)
        copyfile(segmentation_file, destination_segmentation_file)
        t1_file = current_folder + '/T1w_brain.nii.gz'
        t1_destination_file = \
            "{}/images/{}_{}_0000.nii.gz".format(destination_dir, sub_folder, template_folder)
        copyfile(t1_file, t1_destination_file)
        t2_file = current_folder + '/T2w_brain.nii.gz'
        t2_destination_file = \
            "{}/images/{}_{}_0001.nii.gz".format(destination_dir, sub_folder, template_folder)
        copyfile(t2_file, t2_destination_file)
