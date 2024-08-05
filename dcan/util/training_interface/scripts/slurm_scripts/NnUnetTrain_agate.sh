#!/bin/bash
sbatch <<EOT
#!/bin/sh

### Argument to this script is the fold number (between 0 and 4 
### inclusive) and -A argument 
### Sample invocation: ./NnUnetTrain_agate.sh 0 feczk001 545 /raw/data/base/path/ [-c]

#SBATCH --job-name=$3_$1_Train_nnUNet # job name

#SBATCH --mem=90g        # memory per cpu-core (what is the default?)
#SBATCH --time=96:00:00          # total run time limit (HH:MM:SS)
#SBATCH -p a100-4     
#SBATCH --gres=gpu:a100:1
#SBATCH --ntasks=6               # total number of tasks across all nodes

#SBATCH -e Train_$1_$3_nnUNet-%j.err
#SBATCH -o Train_$1_$3_nnUNet-%j.out

#SBATCH -A $2

## build script here
module load gcc cuda/11.2
source /common/software/install/migrated/anaconda/anaconda3-2018.12/etc/profile.d/conda.sh
module load conda
conda activate /home/support/public/pytorch_1.11.0_agate

export nnUNet_raw_data_base="$4"
export nnUNet_preprocessed="$4nnUNet_preprocessed"
export RESULTS_FOLDER="/home/faird/shared/data/nnUNet_lundq163/nnUNet_raw_data_base/nnUNet_trained_models/"

nnUNet_train 3d_fullres nnUNetTrainerV2_noMirroring $3 $1 $5
EOT
