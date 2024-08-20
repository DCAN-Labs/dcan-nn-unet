#!/bin/sh

### Argument to this script is: 
### Sample invocation:

#SBATCH --job-name=create_min_maxes
#SBATCH --time=8:00:00          # total run time limit (HH:MM:SS)
#SBATCH --mem-per-cpu=8GB
#SBATCH --cpus-per-task=4
#SBATCH -A faird
#SBATCH --tmp=20gb
#SBATCH -p msismall

#SBATCH -e Create_min_maxes-%j.err
#SBATCH -o Create_min_maxes-%j.out

## build script here

source /home/faird/shared/code/external/envs/miniconda3/load_miniconda3.sh
conda activate SynthSeg-fixed-perms

export PYTHONPATH=${PYTHONPATH}:$1
export PYTHONPATH=${PYTHONPATH}:$1SynthSeg/

cd $1

python ./SynthSeg/dcan/ten_fold_uniformity_estimation_one_task.py $2 $3
