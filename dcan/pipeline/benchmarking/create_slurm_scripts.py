import os

slurm_script_dir = '/home/feczk001/shared/projects/nnunet_predict/BCP/benchmark/slurm_scripts/'

script = """#!/bin/bash
#SBATCH --job-name=single-input-gpu-infer-{} # job name

#SBATCH -p v100
#SBATCH --gres=gpu:v100:1
#SBATCH --ntasks=3               # total number of tasks across all nodes
#SBATCH --mem=45gb
#SBATCH -t 01:00:00

#SBATCH --mail-type=begin        # send email when job begins
#SBATCH --mail-type=end          # send email when job ends
#SBATCH --mail-user=reine097@umn.edu
#SBATCH -e single-input-gpu-infer-{}-%j.err
#SBATCH -o single-input-gpu-infer-{}-%j.out

#SBATCH -A rando149

## build script here
module load gcc cuda/11.2
source /panfs/roc/msisoft/anaconda/anaconda3-2018.12/etc/profile.d/conda.sh
conda activate /home/support/public/torch_cudnn8.2

nnUNet_predict -i /home/feczk001/shared/projects/nnunet_predict/BCP/benchmark/{}/in/ -o /home/feczk001/shared/projects/nnunet_predict/BCP/benchmark/{}/out/ -t 512 -m 3d_fullres
"""

for i in range(20):
    i_str = str(i).zfill(2)
    blanks_filled_in = script.format(i_str, i_str, i_str, i_str, i_str)
    file_name = 'slurm_script_{}.sh'.format(i_str)
    with open(os.path.join(slurm_script_dir, file_name), "w") as text_file:
        text_file.write(blanks_filled_in)
