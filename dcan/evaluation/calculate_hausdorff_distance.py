"""Usage: calculate_hausdorff_distance <labeled_file_1> <labeled_file_2>"""


from scipy.spatial.distance import directed_hausdorff
import nibabel as nib

labeled_file_1 = '/home/feczk001/shared/data/nnUNet/labelsTs/Task512/8mo_sub-890518.nii.gz'
labeled_file_2 = '/home/feczk001/shared/data/nnUNet/segmentations/inferred/Task512_BCP_ABCD_Neonates_SynthSegDownsample/original/8mo_sub-890518.nii.gz'

# 2   Left-Cerebral-White-Matter

img1 = nib.load(labeled_file_1)
u = img1.get_data()
img2 = nib.load(labeled_file_2)
v = img2.get_data()

hausdorff_distance = max(directed_hausdorff(u, v)[0], directed_hausdorff(v, u)[0])
print(hausdorff_distance)
