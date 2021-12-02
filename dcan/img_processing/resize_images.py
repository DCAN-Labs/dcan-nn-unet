"""
Resize Images.

Usage:
  resize_images <input_folder> <output_folder>
  resize_images -h | --help

Options:
  -h --help     Show this screen.
"""

import os
from os import listdir
from os.path import isfile, join

from docopt import docopt


def resize_images(input_folder, output_folder):
    only_files = [f for f in listdir(input_folder) if isfile(join(input_folder, f))]

    os.system('module load fsl')
    resolution = 1
    for f in only_files:
        input_image = join(input_folder, f)
        print(f)
        command = 'flirt -in {} -ref {} -applyisoxfm {} -init $FSLDIR/etc/flirtsch/ident.mat -o {}'
        reference_image = \
            '/home/feczk001/shared/projects/nnunet_predict/BCP/single_input/input/1mo_sub-nnnnnn_0000.nii.gz'
        output_image = join(output_folder, f)
        filled_in_command = command.format(input_image, reference_image, resolution, output_image)
        os.system(filled_in_command)


if __name__ == '__main__':
    args = docopt(__doc__)
    resize_images(args['<input_folder>'], args['<output_folder>'])
