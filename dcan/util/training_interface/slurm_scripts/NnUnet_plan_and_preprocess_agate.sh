#!/bin/sh

### Argument to this script is the fold number (between 0 and 4 
### inclusive) and -A argument 
### Sample invocation: ./NnUnetTrain_mesabi.sh 0 [-c]

#SBATCH --job-name=545_plan_and_preprocess # job name
#SBATCH --time=24:00:00          # total run time limit (HH:MM:SS)

#SBATCH --mem=90g        # memory per cpu-core (what is the default?)
#SBATCH --time=24:00:00          # total run time limit (HH:MM:SS)
#SBATCH -p a100-4     
#SBATCH --gres=gpu:a100:1
#SBATCH --ntasks=6               # total number of tasks across all nodes

#SBATCH -e Train_545_plan_and_preprocess-%j.err
#SBATCH -o Train_545_plan_and_preprocess-%j.out

module load gcc cuda/11.2
source /common/software/install/migrated/anaconda/anaconda3-2018.12/etc/profile.d/conda.sh
conda activate /home/support/public/torch_cudnn8.2
pip install numpy==1.21.6

export nnUNet_raw_data_base="/scratch.global/lundq163/nnUNet_HBCD_noFlip_noMirr/nnUNet_raw_data_base/"
export nnUNet_preprocessed="/scratch.global/lundq163/nnUNet_HBCD_noFlip_noMirr/nnUNet_raw_data_base/nnUNet_preprocessed/"
export RESULTS_FOLDER="/home/faird/shared/data/nnUNet_lundq163/nnUNet_raw_data_base/nnUNet_trained_models/"
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/common/software/install/migrated/cudnn/8.2.0/lib64

nnUNet_plan_and_preprocess -t 545 --verify_dataset_integrity