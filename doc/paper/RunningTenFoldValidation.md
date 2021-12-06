Running one fold of ten-fold validation
=======================================

If you haven't read the [nnU-Net documentation](https://github.com/MIC-DKFZ/nnUNet#how-to-run-nnu-net-on-a-new-dataset), you should read that first.  It will
save some time, repetition, and confusion.

Note that we're using the 
word *fold* in two different ways:

* [Five folds](https://github.com/MIC-DKFZ/nnUNet#3d-full-resolution-u-net) are run when training a single nnU-Net model.
* We are creating ten models (i.e., running ten tasks), 516--525, each of which is a 'fold' of the 'real' data we have available.  We have split this data into ten folds stratified by age.

There are ten tasks, one for each of the ten folds:

* Task516_Paper_Fold0
* Task517_Paper_Fold1
* Task518_Paper_Fold2

     .
     .
     .

* Task525_Paper_Fold9

**For illustrative purposes, let's assume we're going to run Task 518.**  All other tasks are done similarly and can be done in parallel.

Environment
-----------

Make sure you have the following environment variables set:

    export nnUNet_raw_data_base="/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/"
    export nnUNet_preprocessed="/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_preprocessed"
    export RESULTS_FOLDER="/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_trained_models"

Data
----

### Training and test data

Data is in this folder

        /home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task518_Paper_Fold2

The 'real' images and segmentations should already be in these sub-folders

* imagesTr
* labelsTr

I have not copied over the synthetic data for each of the ten tasks.  (I've only done it for Tasks 516, 517, and 518.  We can do as needed so we don't use up too much disk space.  (Can we just use symbolic links for these common files?))
You can get these files from:

* /home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task512_BCP_ABCD_Neonates_SynthSegDownsample/imagesTr/
* /home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task512_BCP_ABCD_Neonates_SynthSegDownsample/labelsTr/

The synthetic images have names of the form SynthSeg_generated_*nnn*_*n*.nii.gz.  **Do not** copy over any 'real' images.
When you are done copying over the synthetic files, you should have this many files in each folder:

* imagesTr: 1628 items
* imagesTs: 20 items (no synthetic images)
* labelsTr: 814 items

Note that we don't use any synthetic images for testing, and, for consistency, we use the same synthetic images across folds/tasks for training.

### dataset.json file

You need to create a dataset.json file as described in ["Dataset conversion instructions"](https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/dataset_conversion.md).
The resulting dataset.json file will probably not work (unless they've fixed their bugs in `generate_dataset_json`).
You can fix dataset.json by running [`fix_json_file`](../../dcan/dataset_conversion/fix_json_file.py).

Experiment planning and preprocessing
-------------------------------------

Experiment planning and preprocessing is described [here](https://github.com/MIC-DKFZ/nnUNet#experiment-planning-and-preprocessing).
If you want to see a sample SLURM script for running this, look here:

    /home/faird/shared/code/internal/nnUNet/slurm_scripts/517_reiners/plan_and_preprocess.sh

I might be using more resources than I need in this script.  If so, please let me know.

Model training
--------------

Model training is described [here](https://github.com/MIC-DKFZ/nnUNet#model-training).

A sample SLURM script is here:

    /home/faird/shared/code/internal/nnUNet/slurm_scripts/517_reiners/NnUnetTrain.sh

There is also some more information [here](../usage/RunningOneFoldOfnnUNet.md).  

Inference
---------

Running inference, in general, is described [here](https://github.com/MIC-DKFZ/nnUNet#run-inference).

TODO Write inference instructions specific to this project.
