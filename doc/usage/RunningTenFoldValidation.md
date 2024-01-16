# Running Ten-Fold Validation

## Ensure all input files are the same size.

All SynthSeg-generated generated image files and all real image files need to be of the same
size.  If they are not, you should run this program:

* abcd-nn-unet/dcan/img_processing/resize_images.py

Here is a sample invocation:

* /scratch.global/lundq163/nnUNet/IntermediateData_forPaul_10_31_2023/ /scratch.global/lundq163/nnUNet/intermediateData_resized/

The first argument is the input folder and the second folder is the output folder.

# Create 10 Task folders

First you must create 10 Task folders, one for each fold, for nnU-Net.

The code to run is 
[here](https://github.com/DCAN-Labs/dcan-nn-unet/blob/main/dcan/paper/create_ten_fold_validation_folders.py).