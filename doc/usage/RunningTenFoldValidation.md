# Running Ten-Fold Validation

You should first read the documentation on [nnU-Net](https://github.com/MIC-DKFZ/nnUNet) and 
[SynthSeg](https://github.com/BBillot/SynthSeg).  All of the information below is, 
in a sense, redundant and can be gleaned from these two GitHub sites (and, in fact, it was).
Nevertheless, the information below should save you some time and headaches and give some DCAN-specific help.

## Ensure all input files are the same size.

All SynthSeg-generated generated image files and all real image files need to be of the same
size.  If they are not, you should run this program:

* [abcd-nn-unet/dcan/img_processing/resize_images.py](https://github.com/DCAN-Labs/dcan-nn-unet/blob/main/dcan/img_processing/resize_images.py)

```
usage: resize_images [-h] input_folder output_folder

Resizes all images in a folder to (182, 218, 182).

positional arguments:
  input_folder
  output_folder
```

Here is a sample set of arguments:

    /scratch.global/lundq163/nnUNet/IntermediateData_forPaul_10_31_2023/ 
    /scratch.global/lundq163/nnUNet/intermediateData_resized/

The first argument is the input folder and the second folder is the output folder.

# Create 10 Task folders

First you must create 10 Task folders, one for each fold, for nnU-Net.

The code to run is 
[here](https://github.com/DCAN-Labs/dcan-nn-unet/blob/main/dcan/paper/create_ten_fold_validation_folders.py).

The arguments are 

    folder = sys.argv[1]
    nnunet_raw_data_folder = '/scratch.global/lundq163/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/'
    task_number = int(sys.argv[2])
    task_name = sys.argv[3]
    synth_seg = bool(sys.argv[4])
    include_t1 = bool(sys.argv[5])
    include_t2 = bool(sys.argv[6])

Note that there is a hard-coded path:

    nnunet_raw_data_folder = '/scratch.global/lundq163/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/'

You should generalize this by making it a command-line argument.

Here are some sample arguments:

    /scratch.global/lundq163/nnUNet/intermediateData_resized/
    540
    "T1_T2"
    ""
    True
    True

## Create min/max files for each fold.

Create 10 mins_maxes_{i}.npy files, one for each fold.  Sample min/max files are here: 

* /home/miran045/reine097/projects/SynthSeg/data/labels_classes_priors/dcan/uniform/540_549

The code to generate min/max files is here:

* [ten_fold_uniformity_estimation.py](https://github.com/DCAN-Labs/SynthSeg/blob/main/SynthSeg/dcan/ten_fold_uniformity_estimation.py)
* [uniform_intensity_estimation_by_age.py](https://github.com/DCAN-Labs/SynthSeg/blob/main/SynthSeg/dcan/uniform_intensity_estimation_by_age.py)

## Generate synthetic images for all ages

Run

* [SynthSeg/dcan/image_generation_for_all_ages.py](https://github.com/DCAN-Labs/SynthSeg/blob/main/SynthSeg/dcan/image_generation_for_all_ages.py)


    usage: SynthSeg [-h] [--starting-age-in-months STARTING_AGE_IN_MONTHS]
                    [--distribution {normal,uniform}]
                    input-dir output-dir min-mask-file
                    number-generated-images-per-age-group
    
    Generates synthetic images from segmented images.
    
    positional arguments:
      input-dir
      output-dir
      min-mask-file
      number-generated-images-per-age-group
    
    optional arguments:
      -h, --help            show this help message and exit
      --starting-age-in-months STARTING_AGE_IN_MONTHS
      --distribution {normal,uniform}
                            distribution of priors (default: normal)
    
    Forked off of BBillot's SynthSeg

Example arguments:
    
    /scratch.global/lundq163/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task540_T1_T2_Fold0/
    /scratch.global/lundq163/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task540_T1_T2_Fold0/SynthSegGenerated
    /home/miran045/reine097/projects/SynthSeg/data/labels_classes_priors/dcan/uniform/540_549/mins_maxes_0.npy
    1000
    --distribution="uniform"

## Running trading for each fold.

See [Running Ten-Fold Validation](https://github.com/DCAN-Labs/dcan-nn-unet/blob/main/doc/usage/RunningTenFoldValidation.md#running-ten-fold-validation)

## Running inference.

See [Running inference (or creating a segmentation)](https://github.com/DCAN-Labs/dcan-nn-unet/blob/main/doc/usage/inference.md#running-inference-or-creating-a-segmentation)
