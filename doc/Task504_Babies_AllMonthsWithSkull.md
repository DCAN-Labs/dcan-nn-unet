# Task504_Babies_AllMonthsWithSkull

I trained this nnU-Net model on 34 training/cross-validation cases of 0- to 8-month-old babies.
The age distribution for the training/cross-validation set was:

| Age (months)      | training set count | 
| ----------- | ----------- |
| 1  | 2        |
| 2 | 6         |
| 6 | 4         |
| 8 | 6         |


The T1, T2, and manually segmented (a.k.a. "ground truth") files are here:

    * /home/miran045/reine097/JLF_templates_testing/wm_JLF_atlases/

The nnU-Net inferred segmentations are available here:

    * /home/feczk001/shared/data/nnUNet/segmentations/inferred/Task501_Babies_AllMonths/

Below are the manual (i.e., ground-truth) segmentations and the segmentations
inferred by the model trained by nnU-Net.

## Images

Here we have the images layered (from top to bottom):

1. Segmentation (100% opacity)
2. T1 (50% opacity)
3. T2

I also added smoothing.

### 1 month: Template 02

Ground-truth sagittal       |  Predicted sagittal
:-------------------------:|:-------------------------:
![](../img/Task504/1mo/Template02/sagittal/ground_truth.jpg)  |  ![](../img/Task504/1mo/Template02/sagittal/inferred.jpg)
![](../img/Task504/1mo/Template02/sagittal/ground_truth_outline.jpg)  |  ![](../img/Task504/1mo/Template02/sagittal/inferred_outline.jpg)

Ground-truth coronal       |  Predicted coronal
:-------------------------:|:-------------------------:
![](../img/Task504/1mo/Template02/coronal/ground_truth.jpg)  |  ![](../img/Task504/1mo/Template02/coronal/inferred.jpg)
![](../img/Task504/1mo/Template02/coronal/ground_truth_outline.jpg)  |  ![](../img/Task504/1mo/Template02/coronal/inferred_outline.jpg)

Ground-truth axial       |  Predicted axial
:-------------------------:|:-------------------------:
![](../img/Task504/1mo/Template02/axial/ground_truth.jpg)  |  ![](../img/Task504/1mo/Template02/axial/inferred.jpg)
![](../img/Task504/1mo/Template02/axial/ground_truth_outline.jpg)  |  ![](../img/Task504/1mo/Template02/axial/inferred_outline.jpg)

Dice coefficient: 0.24640555156759877

### 2 month: Template 03

Ground-truth sagittal       |  Predicted sagittal
:-------------------------:|:-------------------------:
![](../img/Task504/2mo/Template03/sagittal/ground_truth.jpg)  |  ![](../img/Task504/2mo/Template03/sagittal/inferred.jpg)
![](../img/Task504/2mo/Template03/sagittal/ground_truth_outline.jpg)  |  ![](../img/Task504/2mo/Template03/sagittal/inferred_outline.jpg)

Ground-truth coronal       |  Predicted coronal
:-------------------------:|:-------------------------:
![](../img/Task504/2mo/Template03/coronal/ground_truth.jpg)  |  ![](../img/Task504/2mo/Template03/coronal/inferred.jpg)
![](../img/Task504/2mo/Template03/coronal/ground_truth_outline.jpg)  |  ![](../img/Task504/2mo/Template03/coronal/inferred_outline.jpg)

Ground-truth axial       |  Predicted axial
:-------------------------:|:-------------------------:
![](../img/Task504/2mo/Template03/axial/ground_truth.jpg)  |  ![](../img/Task504/2mo/Template03/axial/inferred.jpg)
![](../img/Task504/2mo/Template03/axial/ground_truth_outline.jpg)  |  ![](../img/Task504/2mo/Template03/axial/inferred_outline.jpg)

Dice coefficient: 0.8730519327509725

### 6 month: Template 04

Ground-truth sagittal       |  Predicted sagittal
:-------------------------:|:-------------------------:
![](../img/Task504/6mo/Template04/sagittal/ground_truth.jpg)  |  ![](../img/Task504/6mo/Template04/sagittal/inferred.jpg)
![](../img/Task504/6mo/Template04/sagittal/ground_truth_outline.jpg)  |  ![](../img/Task504/6mo/Template04/sagittal/inferred_outline.jpg)

Ground-truth coronal       |  Predicted coronal
:-------------------------:|:-------------------------:
![](../img/Task504/6mo/Template04/coronal/ground_truth.jpg)  |  ![](../img/Task504/6mo/Template04/coronal/inferred.jpg)
![](../img/Task504/6mo/Template04/coronal/ground_truth_outline.jpg)  |  ![](../img/Task504/6mo/Template04/coronal/inferred_outline.jpg)

Ground-truth axial       |  Predicted axial
:-------------------------:|:-------------------------:
![](../img/Task504/6mo/Template04/axial/ground_truth.jpg)  |  ![](../img/Task504/6mo/Template04/axial/inferred.jpg)
![](../img/Task504/6mo/Template04/axial/ground_truth_outline.jpg)  |  ![](../img/Task504/6mo/Template04/axial/inferred_outline.jpg)

Dice coefficient: 0.8922089516765477

### 8 month: Template 09

Ground-truth sagittal       |  Predicted sagittal
:-------------------------:|:-------------------------:
![](../img/Task501/8mo_Template01/sagittal_gt.jpg)  |  ![](../img/Task501/8mo_Template01/sagittal_inferred.jpg)
![](../img/Task501/8mo_Template01/sagittal_gt_outline.jpg)  |  ![](../img/Task501/8mo_Template01/sagittal_inferred_outline.jpg)

Ground-truth coronal       |  Predicted coronal
:-------------------------:|:-------------------------:
![](../img/Task501/8mo_Template01/coronal_gt.jpg)  |  ![](../img/Task501/8mo_Template01/coronal_inferred.jpg)
![](../img/Task501/8mo_Template01/coronal_gt_outline.jpg)  |  ![](../img/Task501/8mo_Template01/coronal_inferred_outline.jpg)

Ground-truth axial       |  Predicted axial
:-------------------------:|:-------------------------:
![](../img/Task501/8mo_Template01/axial_gt.jpg) |  ![](../img/Task501/8mo_Template01/axial_inferred.jpg)
![](../img/Task501/8mo_Template01/axial_gt_outline.jpg)  |  ![](../img/Task501/8mo_Template01/axial_inferred_outline.jpg)

Dice coefficient: 0.8938236674895363

## Other test cases

| Test case      | Dice coefficient | 
| ----------- | ----------- |
| 00-02mos_Template04      | 0.8989362179879133        |
| 00-02mos_Template17   | 0.9400775783859089        |
| 00-02mos_Template19 | 0.9315040524238632         |
| 8mo_Template07 | 0.8579367247861686         |
| 8mo_Template09 | 0.878052172240119         |
