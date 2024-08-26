import argparse
import os
import shutil
from os.path import isfile, join

import nilearn
from nilearn import image
from tqdm import tqdm


def resize_images(input_folder, output_folder):
    only_files = [f for f in os.listdir(input_folder) if isfile(join(input_folder, f))]
    desired_shape = (182, 218, 182)
    for f in tqdm(only_files):
        file_path = join(input_folder, f)
        smoothed_img = image.load_img(file_path)
        header = smoothed_img.header
        data_shape = header.get_data_shape()
        if data_shape[:3] != desired_shape:
            print(f'Resizing: {f}')
            if f.endswith('_aseg.nii.gz'):
                interpolation = 'nearest'
            else:
                interpolation = 'continuous'
            target_affine = smoothed_img.affine
            resampled = \
                nilearn.image.resample_img(smoothed_img, target_shape=desired_shape, target_affine=target_affine,
                                           interpolation=interpolation)
            resampled.to_filename(os.path.join(output_folder, f))
        else:
            shutil.copy(file_path, output_folder)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='resize_images',
        description='Resizes all images in a folder to (182, 218, 182).',
        epilog='Contact reine097 if you have any questions or run into any problems.')
    parser.add_argument('task_folder')
    
    args = parser.parse_args()
    file_list = ['imagesTr', 'imagesTs', 'labelsTr', 'labelsTs']

    for name in file_list:
        os.rename(os.path.join(args.task_folder,name), os.path.join(args.task_folder,f'{name}_temp'))
    for name in file_list:
        os.mkdir(os.path.join(args.task_folder,name))
    for name in file_list:
        resize_images(os.path.join(args.task_folder,f'{name}_temp'), os.path.join(args.task_folder,name))
    for name in file_list:
        shutil.rmtree(os.path.join(args.task_folder, f'{name}_temp'))
    
