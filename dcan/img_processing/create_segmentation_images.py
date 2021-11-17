import sys
import os

import nibabel as nib
import numpy as np
from PIL import Image
import ntpath

from dcan.util.look_up_tables import get_id_to_rgb


def create_segmentation_images(segmented_file, output_dir):
    img = nib.load(segmented_file)

    img_data = img.get_fdata()
    shape = img_data.shape

    width = shape[0]
    height = shape[1]
    depth = shape[2]
    axial_array = np.zeros([width, height, 3], dtype=np.uint8)
    mapping_file_name = '../../look_up_tables/FreeSurferColorLUT.txt'
    id_to_rgb = get_id_to_rgb(mapping_file_name)
    axial_slice = img_data[:, :, depth // 2]
    for i in range(width):
        for j in range(height):
            axial_array[i][j] = id_to_rgb[int(axial_slice[i][j])]
    axial_img = Image.fromarray(axial_array)
    axial_img = axial_img.rotate(90)
    axial_img.save(os.path.join(output_dir, 'axial.png'))

    coronal_array = np.zeros([width, depth, 3], dtype=np.uint8)
    coronal_slice = img_data[:, height // 2, :]
    for i in range(width):
        for j in range(depth):
            coronal_array[i][j] = id_to_rgb[int(coronal_slice[i][j])]
    coronal = Image.fromarray(coronal_array)
    coronal = coronal.rotate(90)
    coronal.save(os.path.join(output_dir, 'coronal.png'))

    sagittal_array = np.zeros([height, depth, 3], dtype=np.uint8)
    sagittal_slice = img_data[width // 2, :, :]
    for i in range(width):
        for j in range(depth):
            sagittal_array[i][j] = id_to_rgb[int(sagittal_slice[i][j])]
    sagittal = Image.fromarray(sagittal_array)
    sagittal = sagittal.rotate(90)
    sagittal.save(os.path.join(output_dir, 'sagittal.png'))


if __name__ == '__main__':
    create_segmentation_images(sys.argv[1], sys.argv[2])
