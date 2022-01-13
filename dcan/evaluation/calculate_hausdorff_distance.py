"""Usage: calculate_hausdorff_distance <labeled_file_1> <labeled_file_2>"""


from scipy.spatial.distance import directed_hausdorff
import nibabel as nib

from dcan.util.look_up_tables import get_ids

labeled_file_1 = '/home/feczk001/shared/data/nnUNet/labelsTs/Task512/8mo_sub-890518.nii.gz'
labeled_file_2 = \
    '/home/feczk001/shared/data/nnUNet/segmentations/inferred/Task512_BCP_ABCD_Neonates_SynthSegDownsample/original/' \
    '8mo_sub-890518.nii.gz'

def calculate_hausdorff_distances():
    free_surfer_color_lut='../../look_up_tables/Freesurfer_LUT_DCAN.md'
    ids = get_ids(free_surfer_color_lut)
    id_to_hausdorff_distance = {}
    img1 = nib.load(labeled_file_1)
    data1 = img1.get_data()
    img2 = nib.load(labeled_file_2)
    data2 = img2.get_data()

    for id in ids:
        u = []
        v = []
        for i in range(len(data1)):
            for j in range(len(data1[0])):
                for k in range(len(data1[0][0])):
                    if int(data1[i][j][k]) == 2:
                        u.append((i, j, k))
                    if int(data2[i][j][k]) == 2:
                        v.append((i, j, k))

        hausdorff_distance = max(directed_hausdorff(u, v)[0], directed_hausdorff(v, u)[0])
        id_to_hausdorff_distance[id] = hausdorff_distance

    return id_to_hausdorff_distance
