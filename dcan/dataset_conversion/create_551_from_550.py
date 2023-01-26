import os
from os import listdir
from os.path import isfile, join
import re
import shutil


def main():
    nnuUNet_dir = '/home/feczk001/shared/data/nnUNet'
    nnUNet_raw_data_dir = os.path.join(nnuUNet_dir, 'nnUNet_raw_data_base/nnUNet_raw_data/')
    generated_anatomical_reg_ex = r".*_SynthSeg_generated_(\d\d\d\d)_\d\d\d\d\.nii\.gz"
    generated_labels_reg_ex = r"\dmo_SynthSeg_generated_(\d\d\d\d)\.nii\.gz"
    p_anatomical = re.compile(generated_anatomical_reg_ex)
    p_label = re.compile(generated_labels_reg_ex)
    src_dirs = \
        [os.path.join(nnUNet_raw_data_dir, 'Task550/imagesTr'),
         os.path.join(nnUNet_raw_data_dir, 'Task550/imagesTs'),
         os.path.join(nnUNet_raw_data_dir, 'Task550/labelsTr'),
         os.path.join(nnuUNet_dir, 'labelsTs/550')]
    dest_dirs = \
        [os.path.join(nnUNet_raw_data_dir, 'Task551/imagesTr'),
         os.path.join(os.path.join(nnUNet_raw_data_dir, 'Task551/imagesTs')),
         os.path.join(nnUNet_raw_data_dir, 'Task551/labelsTr'),
         os.path.join(nnuUNet_dir, 'Task551/labelsTs')]
    for i in range(4):
        src_dir = src_dirs[i]
        dest_dir = dest_dirs[i]
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        if 'labels' in src_dir:
            file_type = 'label'
        else:
            file_type = 'anat'
        src_files = [f for f in listdir(src_dir) if isfile(join(src_dir, f))]
        for f in src_files:
            if 'SynthSeg_generated' in f:
                if file_type == 'anat':
                    m = p_anatomical.match(f)
                    index = int(m.group(1))
                    if m:
                        if index % 2 == 1:
                            src_file_name = m.group(0)
                            dest_file = os.path.join(dest_dir, src_file_name)
                            if not os.path.exists(dest_file):
                                shutil.copy(os.path.join(src_dir, src_file_name), dest_dir)
                else:
                    m = p_label.match(f)
                    index = int(m.group(1))
                    if m:
                        if index % 2 == 1:
                            src_file_name = m.group(0)
                            dest_file = os.path.join(dest_dir, src_file_name)
                            if not os.path.exists(dest_file):
                                shutil.copy(os.path.join(src_dir, src_file_name), dest_dir)
            else:
                src_file_name = os.path.join(src_dir, f)
                dest_file = os.path.join(dest_dir, f)
                if not os.path.exists(dest_file):
                    shutil.copy(os.path.join(src_dir, src_file_name), dest_dir)


if __name__ == "__main__":
    main()
