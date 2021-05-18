#!/bin/bash -l
#SBATCH --time=16:00:00
#SBATCH --ntasks=8
#SBATCH --mem=16g
#SBATCH --tmp=8g
#SBATCH --mail-type=ALL
#SBATCH --mail-user=reine097@umn.edu
#SBATCH -p k40
#SBATCH --gres=gpu:k40:1
cd ~ || exit
module load gcc cuda/11.2
source /panfs/roc/msisoft/anaconda/anaconda3-2018.12/etc/profile.d/conda.sh
cd ~/projects/nnUNet/nnunet/run || exit
mpirun -np 8 ~/nnunet-env/bin/python ~/projects/nnUNet/nnunet/run/run_training.py 3d_fullres nnUNetTrainerV2 2 0 > run_training_output.txt
