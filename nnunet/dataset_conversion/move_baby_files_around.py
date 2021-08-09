import os
from shutil import copyfile
import sys


def main(origin_folder, destination_folder):
    for sub_folder in os.listdir(origin_folder):
        for template_folder in os.listdir(origin_folder + '/' + sub_folder):
            if template_folder == 'T2w_files':
                continue
            current_folder = os.path.join(origin_folder, sub_folder, template_folder)
            t1_file = os.path.join(current_folder, 'T1w_acpc_dc_restore.nii.gz')
            t1_destination_file = \
                "{}/images/{}_{}_0000.nii.gz".format(destination_folder, sub_folder, template_folder)
            copyfile(t1_file, t1_destination_file)
            t2_file = os.path.join(origin_folder, sub_folder, 'T2w_files', template_folder + '_T2w_acpc_dc_restore.nii.gz')
            t2_destination_file = \
                "{}/images/{}_{}_0001.nii.gz".format(destination_folder, sub_folder, template_folder)
            copyfile(t2_file, t2_destination_file)


if __name__ == "__main__":
    origin_dir = sys.argv[1]
    destination_dir = sys.argv[2]
    main(origin_dir, destination_dir)
