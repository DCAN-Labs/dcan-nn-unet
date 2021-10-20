% Segmentation with deep learning
% Paul Reiners
% 10/20/2021

### BCP_ABCD_Neonates_Augmentation


* Deep learning segmentation with `nnU-Net` and `lab2im`
* **avg dice: 0.88**
* 5 augmented images per genuine image

---

### 0 month: Template 19
#### Dice (foreground): 0.89

|             | coronal     | sagittal (45) | axial
| ----------- | ----------- | ---- | --- 
| ground-truth      | ![](0mo_template19_coronal_ground_truth_128.jpg)        | ![](0mo_template19_sagittal_ground_truth_128.jpg) | ![](0mo_template19_axial_ground_truth_128.jpg)
| predicted   | ![](0mo_template19_coronal_inferred_128.jpg)        | ![](0mo_template19_sagittal_inferred_128.jpg) | ![](0mo_template19_axial_inferred_128.jpg)

---

### 4 month: Subject 1
#### Dice (foreground): 0.84

|             | coronal     | sagittal (75) | axial
| ----------- | ----------- | ---- | --- 
| ground-truth      | ![](4mo_subject01_coronal_ground_truth_128.jpg)        | ![](4mo_subject01_sagittal_ground_truth_128.jpg) | ![](4mo_subject01_axial_ground_truth_128.jpg)
| predicted   | ![](4mo_subject01_coronal_inferred_128.jpg)        | ![](4mo_subject01_sagittal_inferred_128.jpg) | ![](4mo_subject01_axial_inferred_128.jpg)

---

### 8 month: Subject 1
#### Dice (foreground): 0.90

|             | coronal     | sagittal (75) | axial
| ----------- | ----------- | ---- | --- 
| ground-truth      | ![](8mo_subject01_coronal_ground_truth_128.jpg)        | ![](8mo_subject01_sagittal_ground_truth_128.jpg) | ![](8mo_subject01_axial_ground_truth_128.jpg)
| predicted   | ![](8mo_subject01_coronal_inferred_128.jpg)        | ![](8mo_subject01_sagittal_inferred_128.jpg) | ![](8mo_subject01_axial_inferred_128.jpg)
