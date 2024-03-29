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

The usage is 

```
usage: create_ten_fold_validation_folders [-h]
                                          folder task_number task_name
                                          synth_seg include_t1 include_t2

Create stratified 10-fold validation folders.

positional arguments:
  folder
  task_number
  task_name
  synth_seg
  include_t1
  include_t2
```

Example args:

`/scratch.global/lundq163/nnUNet/intermediateData_resized/ 540 "T1_T2" "" True True`

Note that there is a hard-coded path:

    nnunet_raw_data_folder = '/scratch.global/lundq163/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/'

This should be read in at run-time from the system setting `nnUNet_raw_data_base`.

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

```
usage: ten_fold_uniformity_estimation [-h]

Creates SynthSeg uniform priors for ten-fold validation.
```

* [uniform_intensity_estimation_by_age.py](https://github.com/DCAN-Labs/SynthSeg/blob/main/SynthSeg/dcan/uniform_intensity_estimation_by_age.py) This code is called from `ten_fold_uniformity_estimation` (above).

## Generate synthetic images for all ages

Run

* [SynthSeg/dcan/image_generation_for_all_ages.py](https://github.com/DCAN-Labs/SynthSeg/blob/main/SynthSeg/dcan/image_generation_for_all_ages.py)

```
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
```

Example arguments:
    
    /scratch.global/lundq163/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task540_T1_T2_Fold0/
    /scratch.global/lundq163/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task540_T1_T2_Fold0/SynthSegGenerated
    /home/miran045/reine097/projects/SynthSeg/data/labels_classes_priors/dcan/uniform/540_549/mins_maxes_0.npy
    1000
    --distribution="uniform"

## Running training for each fold.

See [Running a single task](https://github.com/DCAN-Labs/dcan-nn-unet/blob/main/doc/usage/RunningOneFoldOfnnUNet.md)

## Running inference.

See [Running inference (or creating a segmentation)](https://github.com/DCAN-Labs/dcan-nn-unet/blob/main/doc/usage/inference.md#running-inference-or-creating-a-segmentation)

## Create T1-only folders

To create T1-only 10-fold validation folders from T1/T2 10-fold validation folders run  
[create_t1_ten_fold_validation_from_t1_t2_ten_fold_validation.py](https://github.com/DCAN-Labs/dcan-nn-unet/blob/main/dcan/paper/create_t1_ten_fold_validation_from_t1_t2_ten_fold_validation.py).

Useage:

```
usage: create_t1_ten_fold_validation_from_t1_t2_ten_fold_validation
       [-h]
       parent_source_folder first_source_task_number parent_destination_folder
       first_destination_task_number

Create stratified 10-fold validation folders of T1 images from T1/T2 images.

positional arguments:
  parent_source_folder
  first_source_task_number
  parent_destination_folder
  first_destination_task_number

optional arguments:
  -h, --help            show this help message and exit
```

Sample args:

```
/scratch.global/lundq163/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data
540
/scratch.global/lundq163/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data
550
```

## Create T2-only folders

To create T2-only 10-fold validation folders from T2/T2 10-fold validation folders run  
[create_t1_ten_fold_validation_from_t1_t2_ten_fold_validation.py](https://github.com/DCAN-Labs/dcan-nn-unet/blob/main/dcan/paper/create_t1_ten_fold_validation_from_t1_t2_ten_fold_validation.py).

Useage:

```
usage: create_t1_ten_fold_validation_from_t1_t2_ten_fold_validation
       [-h]
       parent_source_folder first_source_task_number parent_destination_folder
       first_destination_task_number

Create stratified 10-fold validation folders of T2 images from T2/T2 images.

positional arguments:
  parent_source_folder
  first_source_task_number
  parent_destination_folder
  first_destination_task_number

optional arguments:
  -h, --help            show this help message and exit
```

Sample args:

```
/scratch.global/lundq163/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data
540
/scratch.global/lundq163/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data
560
```
