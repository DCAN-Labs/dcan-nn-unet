#!/bin/bash

# > segment_images_create_stats_plots <input_image_folder> <output_segmentation_folder> <ground_truth_segmentation_folder> <metrics_results_folder>

# Run on mesabi or agate. Only tested on mesabi.

# Segmentation
module load gcc cuda/11.2
source /panfs/roc/msisoft/anaconda/anaconda3-2018.12/etc/profile.d/conda.sh
conda activate /home/support/public/torch_cudnn8.2

export nnUNet_raw_data_base="/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base"
export nnUNet_preprocessed="/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_preprocessed"
export RESULTS_FOLDER="/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_trained_models"

nnUNet_predict -i $1 -o $2 -t 512 -m 3d_fullres

export PYTHONPATH=${PYTHONPATH}:/home/miran045/reine097/projects/nnUNet/nnunet
/home/miran045/reine097/projects/SynthSeg/venv/bin/python /home/miran045/reine097/projects/SynthSeg/SynthSeg/dcan/paper/evaluate_results_for_folds.py $3 $2 $4

# Created metrics file and plot.
