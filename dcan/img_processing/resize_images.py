import sys
from os import listdir
from os.path import isfile, join
import os


def resize_images(path, output_folder):
    only_files = [f for f in listdir(path) if isfile(join(path, f))]

    os.system('module load fsl')
    resolution = 1
    for f in only_files:
        input_image = join(path, f)
        print(f)
        command = 'flirt -in {} -ref {} -applyisoxfm {} -init $FSLDIR/etc/flirtsch/ident.mat -o {}'
        reference_image = \
            '/home/feczk001/shared/projects/nnunet_predict/BCP/single_input/input/1mo_sub-439083_0000.nii.gz'
        output_image = join(output_folder, f)
        filled_in_command = command.format(input_image, reference_image, resolution, output_image)
        os.system(filled_in_command)


if __name__ == '__main__':
    resize_images(sys.argv[1], sys.argv[2])
