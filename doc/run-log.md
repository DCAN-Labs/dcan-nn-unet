# 2D U-Net

* Fold 0
    * STARTED: 4/26/2021
    * `srun --time=16:00:00 --ntasks=1 --mem=32g --tmp=40g -p v100 --gres=gpu:v100:1 nnUNet_train 2d  nnUNetTrainerV2 2 0`