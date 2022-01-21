"""
Resize Images.

Usage:
  resize_images <input_folder> <output_folder> <flirt_path>
  resize_images -h | --help

Options:
  -h --help     Show this screen.
"""

import os
from os import listdir
from os.path import isfile, join
import subprocess
import sys


def resize_images(input_folder, output_folder, flirt_path):
    os.system('module load fsl')
    only_files = [f for f in listdir(input_folder) if isfile(join(input_folder, f))]

    t1_suffix = '_0000.nii.gz'
    t2_suffix = '_0001.nii.gz'
    for f in only_files:
        if f.endswith('_0000.nii.gz'):
            in_path = join(input_folder, f)
            ref_path = join(input_folder, f[:-len(t1_suffix)] + t2_suffix)
            print('in_path: ', in_path)
            print('ref_path:', ref_path)
            try:
                subprocess.check_call([flirt_path, '-interp', 'spline', '-in',
                                       in_path, '-ref', ref_path])
            except Exception as err:
                print('Error:', err)

    resolution = 1
    for f in only_files:
        input_image = join(input_folder, f)
        print(f)
        command = '{} -in {} -ref {} -applyisoxfm {} -init $FSLDIR/etc/flirtsch/ident.mat -o {}'
        reference_image = \
            '/home/feczk001/shared/projects/nnunet_predict/BCP/single_input/input/1mo_sub-nnnnnn_0000.nii.gz'
        output_image = join(output_folder, f)
        filled_in_command = command.format(flirt_path, input_image, reference_image, resolution, output_image)
        os.system(filled_in_command)


if __name__ == '__main__':
    args = sys.argv
    resize_images(args[1], args[2], args[3])
