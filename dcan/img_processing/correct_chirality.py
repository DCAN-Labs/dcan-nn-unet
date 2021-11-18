import nibabel as nib
import sys

from dcan.util.look_up_tables import get_id_to_region_mapping

RIGHT = 'Right'

LEFT = 'Left'


def check_and_correct_region(should_be_left, region, segment_name_to_number, new_data, chirality,
                             floor_ceiling, scanner_bore):
    if should_be_left:
        expected_prefix = LEFT
        wrong_prefix = RIGHT
    else:
        expected_prefix = RIGHT
        wrong_prefix = LEFT
    if region.startswith(wrong_prefix):
        flipped_region = expected_prefix + region[len(wrong_prefix):]
        flipped_id = segment_name_to_number[flipped_region]
        new_data[chirality][floor_ceiling][scanner_bore] = flipped_id


def correct_chirality(nifti_input_file_path, segment_lookup_table, nifti_output_file_path):
    free_surfer_label_to_region = get_id_to_region_mapping(segment_lookup_table)
    segment_name_to_number = {v: k for k, v in free_surfer_label_to_region.items()}
    img = nib.load(nifti_input_file_path)
    data = img.get_data()

    M = img.affine[:3, :3]
    abc = img.affine[:3, 3]

    def f(i, j, k):
        """ Return X, Y, Z coordinates for i, j, k """
        return M.dot([i, j, k]) + abc

    new_data = data.copy()
    data_shape = img.header.get_data_shape()
    max_i = data_shape[0]
    for i in range(max_i):
        max_j = data_shape[1]
        for j in range(max_j):
            max_k = data_shape[2]
            for k in range(max_k):
                x, y, z = f(i, j, k)
                voxel = data[i][j][k]
                if voxel == 0:
                    continue
                region = free_surfer_label_to_region[voxel]
                if x <= 0:
                    check_and_correct_region(True, region, segment_name_to_number, new_data, i,
                                             j, k)
                else:
                    check_and_correct_region(False, region, segment_name_to_number, new_data, i,
                                             j, k)
    fixed_img = nib.Nifti1Image(new_data, img.affine, img.header)
    nib.save(fixed_img, nifti_output_file_path)


if __name__ == "__main__":
    correct_chirality(sys.argv[1], sys.argv[2], sys.argv[3])
