#!/bin/bash
sbatch <<EOT
#!/bin/sh

### Argument to this script is the fold number (between 0 and 4 
### inclusive) and -A argument 
### Sample invocation: ./NnUnetTrain_agate.sh 0 feczk001 [-c]

#SBATCH --job-name=542_$1_Train_nnUNet # job name

#SBATCH --mem=90g        # memory per cpu-core (what is the default?)
#SBATCH --time=96:00:00          # total run time limit (HH:MM:SS)
#SBATCH -p a100-4     
#SBATCH --gres=gpu:a100:1
#SBATCH --ntasks=6               # total number of tasks across all nodes

#SBATCH --mail-type=begin        # send 7mail when job begins
#SBATCH --mail-type=end          # send email when job ends
#SBATCH --mail-user=efair@umn.edu
#SBATCH -e Train_$1_542_nnUNet-%j.err
#SBATCH -o Train_$1_542_nnUNet-%j.out

#SBATCH -A $2

## build script here
module load gcc cuda/11.2
source /common/software/install/migrated/anaconda/anaconda3-2018.12/etc/profile.d/conda.sh
module load conda
conda activate /home/support/public/pytorch_1.11.0_agate

export nnUNet_raw_data_base="/scratch.global/lundq163/nnUNet_HBCD_noFlip_noMirr/nnUNet_raw_data_base/"
export nnUNet_preprocessed="/scratch.global/lundq163/nnUNet_HBCD_noFlip_noMirr/nnUNet_raw_data_base/nnUNet_preprocessed/"
export RESULTS_FOLDER="/home/faird/shared/data/nnUNet_lundq163/nnUNet_raw_data_base/nnUNet_trained_models/"

nnUNet_train 3d_fullres nnUNetTrainerV2_noMirroring 542 $1 $3
EOT
