# Task504_Babies_AllMonthsWithSkull

I trained this nnU-Net model on 14 training cases of 1- to 8-month-old babies.
The age distribution for the training set was:

| Age (months)      | training set count | 
| ----------- | ----------- |
| 1  | 1        |
| 2 | 2         |
| 6 | 3         |
| 8 | 8         |

The T1 and T2 files are here:

    * /home/feczk001/shared/data/nnUNet/JLF_templates_testing/wm_JLF_atlases/head_files/

The manually segmented (a.k.a. "ground truth") files are here:

    * /home/feczk001/shared/data/nnUNet/JLF_templates_testing/wm_JLF_atlases/

The nnU-Net inferred segmentations are available here:

    * /home/feczk001/shared/data/nnUNet/segmentations/Task504_AllAgesWithSkull/predictions/

## Images

Here we have the images layered (from top to bottom):

1. Segmentation (100% opacity)
2. T1 (50% opacity)
3. T2

I also added smoothing.

### 1 month: Template 02

Ground-truth sagittal       |  Predicted sagittal
:-------------------------:|:-------------------------:
![](../../img/Task504/1mo/Template02/sagittal/ground_truth.jpg)  |  ![](../../img/Task504/1mo/Template02/sagittal/inferred.jpg)
![](../../img/Task504/1mo/Template02/sagittal/ground_truth_outline.jpg)  |  ![](../../img/Task504/1mo/Template02/sagittal/inferred_outline.jpg)

Ground-truth coronal       |  Predicted coronal
:-------------------------:|:-------------------------:
![](../../img/Task504/1mo/Template02/coronal/ground_truth.jpg)  |  ![](../../img/Task504/1mo/Template02/coronal/inferred.jpg)
![](../../img/Task504/1mo/Template02/coronal/ground_truth_outline.jpg)  |  ![](../../img/Task504/1mo/Template02/coronal/inferred_outline.jpg)

Ground-truth axial       |  Predicted axial
:-------------------------:|:-------------------------:
![](../../img/Task504/1mo/Template02/axial/ground_truth.jpg)  |  ![](../../img/Task504/1mo/Template02/axial/inferred.jpg)
![](../../img/Task504/1mo/Template02/axial/ground_truth_outline.jpg)  |  ![](../../img/Task504/1mo/Template02/axial/inferred_outline.jpg)

Dice coefficient: 0.24640555156759877

### 2 month: Template 03

Ground-truth sagittal       |  Predicted sagittal
:-------------------------:|:-------------------------:
![](../../img/Task504/2mo/Template03/sagittal/ground_truth.jpg)  |  ![](../../img/Task504/2mo/Template03/sagittal/inferred.jpg)
![](../../img/Task504/2mo/Template03/sagittal/ground_truth_outline.jpg)  |  ![](../../img/Task504/2mo/Template03/sagittal/inferred_outline.jpg)

Ground-truth coronal       |  Predicted coronal
:-------------------------:|:-------------------------:
![](../../img/Task504/2mo/Template03/coronal/ground_truth.jpg)  |  ![](../../img/Task504/2mo/Template03/coronal/inferred.jpg)
![](../../img/Task504/2mo/Template03/coronal/ground_truth_outline.jpg)  |  ![](../../img/Task504/2mo/Template03/coronal/inferred_outline.jpg)

Ground-truth axial       |  Predicted axial
:-------------------------:|:-------------------------:
![](../../img/Task504/2mo/Template03/axial/ground_truth.jpg)  |  ![](../../img/Task504/2mo/Template03/axial/inferred.jpg)
![](../../img/Task504/2mo/Template03/axial/ground_truth_outline.jpg)  |  ![](../../img/Task504/2mo/Template03/axial/inferred_outline.jpg)

Dice coefficient: 0.8730519327509725

### 6 month: Template 04

Ground-truth sagittal       |  Predicted sagittal
:-------------------------:|:-------------------------:
![](../../img/Task504/6mo/Template04/sagittal/ground_truth.jpg)  |  ![](../../img/Task504/6mo/Template04/sagittal/inferred.jpg)
![](../../img/Task504/6mo/Template04/sagittal/ground_truth_outline.jpg)  |  ![](../../img/Task504/6mo/Template04/sagittal/inferred_outline.jpg)

Ground-truth coronal       |  Predicted coronal
:-------------------------:|:-------------------------:
![](../../img/Task504/6mo/Template04/coronal/ground_truth.jpg)  |  ![](../../img/Task504/6mo/Template04/coronal/inferred.jpg)
![](../../img/Task504/6mo/Template04/coronal/ground_truth_outline.jpg)  |  ![](../../img/Task504/6mo/Template04/coronal/inferred_outline.jpg)

Ground-truth axial       |  Predicted axial
:-------------------------:|:-------------------------:
![](../../img/Task504/6mo/Template04/axial/ground_truth.jpg)  |  ![](../../img/Task504/6mo/Template04/axial/inferred.jpg)
![](../../img/Task504/6mo/Template04/axial/ground_truth_outline.jpg)  |  ![](../../img/Task504/6mo/Template04/axial/inferred_outline.jpg)

Dice coefficient: 0.8922089516765477

### 8 month: Template 09

Ground-truth sagittal       |  Predicted sagittal
:-------------------------:|:-------------------------:
![](../../img/Task504/8mo/Template09/sagittal/ground_truth.jpg)  |  ![](../../img/Task504/8mo/Template09/sagittal/inferred.jpg)
![](../../img/Task504/8mo/Template09/sagittal/ground_truth_outline.jpg)  |  ![](../../img/Task504/8mo/Template09/sagittal/inferred_outline.jpg)

Ground-truth coronal       |  Predicted coronal
:-------------------------:|:-------------------------:
![](../../img/Task504/8mo/Template09/coronal/ground_truth.jpg)  |  ![](../../img/Task504/8mo/Template09/coronal/inferred.jpg)
![](../../img/Task504/8mo/Template09/coronal/ground_truth_outline.jpg)  |  ![](../../img/Task504/8mo/Template09/coronal/inferred_outline.jpg)

Ground-truth axial       |  Predicted axial
:-------------------------:|:-------------------------:
![](../../img/Task504/8mo/Template09/axial/ground_truth.jpg)  |  ![](../../img/Task504/8mo/Template09/axial/inferred.jpg)
![](../../img/Task504/8mo/Template09/axial/ground_truth_outline.jpg)  |  ![](../../img/Task504/8mo/Template09/axial/inferred_outline.jpg)

Dice coefficient: 0.8938236674895363
