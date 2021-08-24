import os
import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np


def show_slices(slices, cmap="gray"):
    """ Function to display row of image slices """
    fig, axes = plt.subplots(1, len(slices))
    for i, slc in enumerate(slices):
        axes[i].imshow(slc.T, cmap=cmap, origin="lower")


def get_dcan_lut():
    dcan_lut_file = '/home/miran045/reine097/projects/abcd-nn-unet/doc/Freesurfer_LUT_DCAN.txt'
    file = open(dcan_lut_file, 'r')
    lines = file.readlines()
    dcan_lut = {}
    for line in lines:
        line = line.strip()
        if len(line) == 0 or line[0] == '#':
            continue
        label, _, r, g, b = line.split()
        dcan_lut[label] = (r, g, b)
    file.close()

    return dcan_lut


directory = r'/home/feczk001/shared/data/nnUNet/segmentations/inferred/subjects_to_edit/'
img_dir = '/home/miran045/reine097/projects/abcd-nn-unet/img/subjects_to_edit'
for filename in os.listdir(directory):
    nifti_extension = ".nii.gz"
    if filename.endswith(nifti_extension):
        file_path = os.path.join(directory, filename)
        print(file_path)
        img = nib.load(file_path)
        anat_img_data = img.get_fdata()
        s1, s2, s3 = anat_img_data.shape
        slice1 = anat_img_data[s1 // 2, :, :]
        rgb_slice1 = np.ndarray(slice1.shape, int)
        for i in range(slice1.shape[0]):
            for j in range(slice1.shape[1]):
                # TODO finish
                pass
        slice2 = anat_img_data[:, s2 // 2, :]
        slice3 = anat_img_data[:, :, s3 // 2]
        show_slices([slice1,
                     slice2,
                     slice3],
                    cmap='gray')
        file_name_no_extension = filename[:-len(nifti_extension)]
        title = "Center slices for {} image".format(file_name_no_extension)
        plt.suptitle(title)
        img_path = os.path.join(img_dir, file_name_no_extension + ".jpeg")
        plt.savefig(img_path)
    else:
        continue
