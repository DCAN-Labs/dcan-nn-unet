# Author: Paul Reiners


import os

path = '/home/feczk001/shared/data/nnUNet/labelsTs/Task510/'
os.chdir(path)
os.system('module load fsl')
# os.system('flirt -in 0mo_template_01_0000.nii.gz -ref 1mo_sub-198549_0000.nii.gz -out 0mo_template_01_0000_resized.nii.gz -interp spline -applyisoxfm 1 -init "$FSLDIR/etc/flirtsch/ident.mat"')
os.system('flirt -applyisoxfm 1 -init "$FSLDIR/etc/flirtsch/ident.mat" -in 0mo_template_19.nii.gz -ref 1mo.nii.gz -out 0mo_template_19_resized.nii.gz -interp nearestneighbour')
