Task 509: BCP_ABCD_Neonates
===========================

Data description
----------------

Basecamp task is [here](https://3.basecamp.com/5032058/buckets/21825058/todos/4048241976).

* augmented images per genuine image just like the paper
* use the same distribution for lab2im as the paper (normal distribution)
* skull is on for all of them, including for the augmented images

## Training

The data is in the union of these two folders:

* `/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task509_BCP_ABCD_Neonates/`
* `/home/feczk001/shared/data/nnUNet/labelsTs/Task509/`

The age distribution for the training set was:

| Age (months)      | training set count | 
| ----------- | ----------- |
| 0  | 18        |
| 1  | 2        |
| 2 | 6         |
| 3 | 7         |
| 4 | 5         |
| 5 | 9         |
| 6 | 8         |
| 7 | 9         |
| 8 | 8         |

## Test

Images below are layered (from top to bottom):

1. Segmentation (100% opacity)
2. T1 (50% opacity)
3. T2

I also added smoothing.

### 0 month: Example 1

Ground-truth sagittal       |  Predicted sagittal
:-------------------------:|:-------------------------:
![](../../img/Task509/0mo/sub-1/sagittal/ground_truth.jpg)  |  ![](../../img/Task509/0mo/sub-1/sagittal/inferred.jpg)
![](../../img/Task509/0mo/sub-1/sagittal/ground_truth_outline.jpg)  |  ![](../../img/Task509/0mo/sub-1/sagittal/inferred_outline.jpg)

Ground-truth coronal       |  Predicted coronal
:-------------------------:|:-------------------------:
![](../../img/Task509/0mo/sub-1/coronal/ground_truth.jpg)  |  ![](../../img/Task509/0mo/sub-1/coronal/inferred.jpg)
![](../../img/Task509/0mo/sub-1/coronal/ground_truth_outline.jpg)  |  ![](../../img/Task509/0mo/sub-1/coronal/inferred_outline.jpg)

Ground-truth axial       |  Predicted axial
:-------------------------:|:-------------------------:
![](../../img/Task509/0mo/sub-1/axial/ground_truth.jpg)  |  ![](../../img/Task509/0mo/sub-1/axial/inferred.jpg)
![](../../img/Task509/0mo/sub-1/axial/ground_truth_outline.jpg)  |  ![](../../img/Task509/0mo/sub-1/axial/inferred_outline.jpg)

Dice coefficient: 0.xxx
