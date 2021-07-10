#!/bin/bash
#SBATCH --job-name=502_infer # job name
#SBATCH --mem=64g        # memory per cpu-core (what is the default?)
#SBATCH --time=1:00:00          # total run time limit (HH:MM:SS)

#SBATCH -p v100
#SBATCH --gres=gpu:v100:2
#SBATCH --ntasks=1               # total number of tasks across all nodes
#SBATCH --tmp=40g
#SBATCH --cpus-per-task=24

#SBATCH --mail-type=begin        # send email when job begins
#SBATCH --mail-type=end          # send email when job ends
#SBATCH --mail-user=reine097@umn.edu
#SBATCH -e infer_502-%j.err
#SBATCH -o infer_502-%j.out

## build script here
module load gcc cuda/11.2
source /panfs/roc/msisoft/anaconda/anaconda3-2018.12/etc/profile.d/conda.sh
conda activate /home/support/public/torch_cudnn8.2

nnUNet_predict -i $nnUNet_raw_data_base/nnUNet_raw_data/Task502_Babies_AllMonthsAgeNotEncoded/imagesTs/ -o /home/feczk001/shared/data/nnUNet/segmentations/inferred/Task502_Babies_AllMonthsAgeNotEncoded/ -t 502 -m 3d_fullres
