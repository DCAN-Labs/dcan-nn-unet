Preprocessing and postprocessing of images
========================================

The models are trained on images of size 182 x 218 x 182.  I've found that if you 
run inference on images of a different size, nnU-Net creates some .npy files
in the output folder and then hangs.  I don't know if this is the case for 
every size of image other than 182 x 218 x 182, but it has happened for the
dimensions I have tried, for example, 208 x 300 x 320.  According to the nnU-Net maintainers,
using images of a different size for inference should not matter.  See [Issue #833](https://github.com/MIC-DKFZ/nnUNet/issues/833).

There are, in general, four steps for running inference.

1. Crop images if the images contain shoulders.  Use [crop_images.py](../../dcan/img_processing/crop_images.py).
2. Resize the images to 182 x 218 x 182.  Use [resize_images.py](../../dcan/img_processing/resize_images.py).
3. Run nnU-Net inference.  See [inference.md](../useage/inference.md) for details.
4. Correct chirality problems.  Use [correct_chirality_for_folder.py](../../dcan/img_processing/correct_chirality_for_folder.py).
