#!/bin/bash
sbatch <<EOT
#!/bin/sh

#SBATCH --job-name=545_infer 
#SBATCH --mem=64g       
#SBATCH --time=8:00:00          # (HH:MM:SS)

#SBATCH -p a100-4     
#SBATCH --gres=gpu:a100:1
#SBATCH --ntasks=1
#SBATCH -e infer_545-%j.err
#SBATCH -o infer_545-%j.out

#SBATCH -A $1

## build script here
module load gcc cuda/11.2
source /common/software/install/migrated/anaconda/anaconda3-2018.12/etc/profile.d/conda.sh
module load conda
conda activate /home/support/public/pytorch_1.11.0_agate


export nnUNet_raw_data_base="/scratch.global/lundq163/nnUNet_HBCD_noFlip_noMirr/nnUNet_raw_data_base/"
export nnUNet_preprocessed="/scratch.global/lundq163/nnUNet_HBCD_noFlip_noMirr/nnUNet_raw_data_base/nnUNet_preprocessed/"
export RESULTS_FOLDER="/home/faird/shared/data/nnUNet_lundq163/nnUNet_raw_data_base/nnUNet_trained_models/"



nnUNet_predict -i /scratch.global/lundq163/nnUNet_HBCD_noFlip_noMirr/nnUNet_raw_data_base/nnUNet_raw_data/Task545/imagesTs -o /home/faird/shared/data/nnUNet_lundq163/545_infer/ -t 545 -tr nnUNetTrainerV2_noMirroring -m 3d_fullres --disable_tta
EOT
