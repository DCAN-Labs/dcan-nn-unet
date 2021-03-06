# Running inference (or creating a segmentation)

Overview
--------

You should read this first: [Example: inference with pretrained nnU-Net models](https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/inference_example_Prostate.md)

The trained model is not set directly, although it is set implicitly.  What you have to pass in is the task number.  An example task number would be `512`.  nnU-Net uses the `RESULTS_FOLDER` environment variable to then find the folder.  I have been using the following setting:

     export RESULTS_FOLDER="/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_trained_models"

Here is a sample inference command:

     nUNet_predict -i /home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task509_BCP_ABCD_Neonates/imagesTs/ -o /home/feczk001/shared/data/nnUNet/segmentations/inferred/Task512_BCP_ABCD_Neonates_SynthSegDownsample/ -t 512 -m 3d_fullres
     
You don't need the entire trained models directory in order to run prediction with nnU-Net.  You only need the directory with the particular model you're using to run prediction.  However, you need to preserve the path to that one directory (even though you're not keeping that directory's siblings).  For example, if you're making predictions using model *512* (and you're using the same environment variables given in the preceding examples), you would need this folder and its contents:

     /home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_trained_models/nnUNet/3d_fullres/Task512_BCP_ABCD_Neonates_SynthSegDownsample/
     
For inference, there is no minimum number of subjects needed.  It should work for 1.  There's no reason why it shouldn't work for 0 subjects, although I haven't tried that (and I don't know whether the maintainers of nnU-Net have tried it).

(For the record, it wouldn't make sense to train without at least one subject.)

The model directory is of size 2.834 GB (gigabytes) adding all files/directories recursively.  It doesn't get larger with a larger training size.  It might get larger with larger image sizes, but I don't think we'll be changing those much, if at all.

Here are typical run times and memory usage:

            JobID     MaxRSS   TotalCPU      NCPUS    Elapsed 
     ------------ ---------- ---------- ---------- ---------- 
     7438367                  51:05.368         24   00:37:23 
     7438367.bat+  44392828K  51:05.367         24   00:37:23 
     7438367.ext+       924K  00:00.001         24   00:37:23 
     
This was for 10 subjects.  Hence, each subject takes about 4 minutes.

Details
-------

Here is an example of running inference on one of our models:

    module load gcc cuda/11.2
    source /panfs/roc/msisoft/anaconda/anaconda3-2018.12/etc/profile.d/conda.sh
    conda activate /home/support/public/torch_cudnn8.2

    nnUNet_predict -i $nnUNet_raw_data_base/nnUNet_raw_data/Task512_BCP_ABCD_Neonates_SynthSegDownsample/imagesTs/ -o /home/feczk001/shared/data/nnUNet/segmentations/inferred/Task512_BCP_ABCD_Neonates_SynthSegDownsample/ -t 506 -m 3d_fullres

`$nnUNet_raw_data_base` is an environment variable you need to set.  Actually, you need to set three environment variables:

    export nnUNet_raw_data_base="/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/"
    export nnUNet_preprocessed="/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_preprocessed"
    export RESULTS_FOLDER="/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_trained_models"

The `-i` (input) argument is the files you want to run inference on.

This is just an example, but, if you look in that folder, you will see:

    -bash-4.2$ ls $nnUNet_raw_data_base/nnUNet_raw_data/Task512_BCP_ABCD_Neonates_SynthSegDownsample/imagesTs/
    0mo_template_19_0000.nii.gz  1mo_sub-439083_0000.nii.gz  3mo_sub-940808_0000.nii.gz  5mo_sub-993015_0000.nii.gz  7mo_updated_sub-786266_0000.nii.gz
    0mo_template_19_0001.nii.gz  1mo_sub-439083_0001.nii.gz  3mo_sub-940808_0001.nii.gz  5mo_sub-993015_0001.nii.gz  7mo_updated_sub-786266_0001.nii.gz
    0mo_template_20_0000.nii.gz  2mo_sub-993015_0000.nii.gz  4mo_sub-710922_0000.nii.gz  6mo_sub-621289_0000.nii.gz  8mo_sub-890518_0000.nii.gz
    0mo_template_20_0001.nii.gz  2mo_sub-993015_0001.nii.gz  4mo_sub-710922_0001.nii.gz  6mo_sub-621289_0001.nii.gz  8mo_sub-890518_0001.nii.gz

The files ending in "0000" are T1 files and those ending in "0001" are T2 files.
This is a naming convention that was specified when the model was created.
 I've written several utility scripts for rearranging files and naming them properly.  
[You can find some of them in this folder](../../dcan/dataset_conversion).
These utility programs *ad hoc* and not necessarily well-commented.  (I.e., I wrote them basically for my own use as needed.)
TODO Make them better.  



The `-o` argument is the output directory for the label files created by the model.
