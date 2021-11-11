import os
import sys

from dcan.img_processing.create_segmentation_images import create_segmentation_images


def create_segmentation_images_for_folder(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".nii.gz"):
            input_file_path = os.path.join(input_folder, filename)
            print(input_file_path)
            create_segmentation_images(input_file_path, output_folder)
        else:
            continue


if __name__ == '__main__':
    create_segmentation_images_for_folder(sys.argv[1], sys.argv[2])
