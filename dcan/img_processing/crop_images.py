"""
Resize Images.

Usage:
  crop_images <input_folder> <output_folder>
  crop_images -h | --help

Options:
  -h --help     Show this screen.
"""

from os import listdir
from os.path import isfile, join

import nibabel as nib
from docopt import docopt


def crop_images(image_dir, output_dir):
    z_max = 320
    z_min = 80
    image_files = sorted([f for f in listdir(image_dir) if isfile(join(image_dir, f))])
    for f in image_files:
        # fslroi sub-CENSORED_ses-20210412_T1w sub-CENSORED_ses-20210412_T1w_cropped 0 144 0 300 103 320
        input_file = join(image_dir, f)
        img = nib.load(input_file)
        cropped_img = img.slicer[:208, :300, z_min:z_max, ...]
        print(cropped_img.shape)
        output_file = join(output_dir, f)
        nib.save(cropped_img, output_file)


if __name__ == '__main__':
    args = docopt(__doc__)
    crop_images(args['<input_folder>'], args['<output_folder>'])
