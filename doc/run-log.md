Run-times
=========

* 1 segmentation
  * Fold 0
    * Queued time:    03:21:42
    * Initialization:

----

# Benchmarking

* `nnUNet_train 2d nnUNetTrainerV2_5epochs 2 0`
    * This epoch took 1288.745074 s
  
* `srun --time=16:00:00 --ntasks=1 --mem=32g --tmp=40g -p v100 --gres=gpu:v100:1 nnUNet_train 2d nnUNetTrainerV2_5epochs 2 0`
    * 322.203758 s

# 2D U-Net

* Fold 0
    * STARTED: 4/26/2021
    * `srun --time=16:00:00 --ntasks=1 --mem=32g --tmp=40g -p v100 --gres=gpu:v100:1 nnUNet_train 2d  nnUNetTrainerV2 2 0`