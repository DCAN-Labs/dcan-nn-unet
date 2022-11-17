Task512_BCP_ABCD_Neonates_SynthSegDownsample
=============================================

Dice coefficient: 0.853262030191724
-----------------

### nnU-Net settings
    "modality": {
        "0": "T1",
        "1": "T2"
    },


### SynthSeg settings

    downsample=True
    prior_distributions='normal'

### Summary

| segment_name      | Dice |
| ----------- | ----------- |
| Cerebral-White-Matter | 0.8569272769753329 | 
| Cerebral-Cortex | 0.8397469274483849 |
| Lateral-Ventricle | 0.8038140272934797 |
| Cerebellum-Cortex | 0.8678992501253581 |
| Thalamus-Proper* | 0.8496686503956972 |
| Caudate | 0.7847380414558429 |
| Putamen | 0.7906269525966562 |
| Pallidum | 0.7536450702975441 |
| 3rd-Ventricle | 0.8769779276317535 |
| 4th-Ventricle | 0.8472866893067705 |
| Brain-Stem | 0.9078272367621212 |
| Hippocampus | 0.7973869532268174 |
| Amygdala | 0.7941830548737976 |
| Accumbens-area | 0.5994838698375999 |
| VentralDC | 0.7839104355039526 |

![Dice scores box plot](dice_scores.png "Dice scores")

* [Detailed statistics stratified by anatomical region](means.csv)

### 0 month: Template 19

Ground-truth coronal       |  Predicted coronal
:-------------------------:|:-------------------------:
![](./img/0mo_template_19/ground_truth/coronal.png)  |  ![](./img/0mo_template_19/inferred/coronal.png)

Ground-truth sagittal       |  Predicted sagittal
:-------------------------:|:-------------------------:
![](./img/0mo_template_19/ground_truth/sagittal.png)  |  ![](./img/0mo_template_19/inferred/sagittal.png)

Ground-truth axial       |  Predicted axial
:-------------------------:|:-------------------------:
![](./img/0mo_template_19/ground_truth/axial.png)  |  ![](./img/0mo_template_19/inferred/axial.png)

Dice (foreground): 0.88

### 0 month: Template 20

Ground-truth coronal       |  Predicted coronal
:-------------------------:|:-------------------------:
![](./img/0mo_template_20/ground_truth/coronal.png)  |  ![](./img/0mo_template_20/inferred/coronal.png)

Ground-truth sagittal       |  Predicted sagittal
:-------------------------:|:-------------------------:
![](./img/0mo_template_20/ground_truth/sagittal.png)  |  ![](./img/0mo_template_20/inferred/sagittal.png)

Ground-truth axial       |  Predicted axial
:-------------------------:|:-------------------------:
![](./img/0mo_template_20/ground_truth/axial.png)  |  ![](./img/0mo_template_20/inferred/axial.png)

Dice (foreground): 0.89

### 1 month

Ground-truth coronal       |  Predicted coronal
:-------------------------:|:-------------------------:
![](./img/1mo/ground_truth/coronal.png)  |  ![](./img/1mo/inferred/coronal.png)

Ground-truth sagittal       |  Predicted sagittal
:-------------------------:|:-------------------------:
![](./img/1mo/ground_truth/sagittal.png)  |  ![](./img/1mo/inferred/sagittal.png)

Ground-truth axial       |  Predicted axial
:-------------------------:|:-------------------------:
![](./img/1mo/ground_truth/axial.png)  |  ![](./img/1mo/inferred/axial.png)

Dice (foreground): 0.90

### 2 month

Ground-truth coronal       |  Predicted coronal
:-------------------------:|:-------------------------:
![](./img/2mo/ground_truth/coronal.png)  |  ![](./img/2mo/inferred/coronal.png)

Ground-truth sagittal       |  Predicted sagittal
:-------------------------:|:-------------------------:
![](./img/2mo/ground_truth/sagittal.png)  |  ![](./img/2mo/inferred/sagittal.png)

Ground-truth axial       |  Predicted axial
:-------------------------:|:-------------------------:
![](./img/2mo/ground_truth/axial.png)  |  ![](./img/2mo/inferred/axial.png)

Dice (foreground): 0.91

### 3 month

Ground-truth coronal       |  Predicted coronal
:-------------------------:|:-------------------------:
![](./img/3mo/ground_truth/coronal.png)  |  ![](./img/3mo/inferred/coronal.png)

Ground-truth sagittal       |  Predicted sagittal
:-------------------------:|:-------------------------:
![](./img/3mo/ground_truth/sagittal.png)  |  ![](./img/3mo/inferred/sagittal.png)

Ground-truth axial       |  Predicted axial
:-------------------------:|:-------------------------:
![](./img/3mo/ground_truth/axial.png)  |  ![](./img/3mo/inferred/axial.png)

Dice (foreground): 0.59

### 4 month

Ground-truth coronal       |  Predicted coronal
:-------------------------:|:-------------------------:
![](./img/4mo/ground_truth/coronal.png)  |  ![](./img/4mo/inferred/coronal.png)

Ground-truth sagittal       |  Predicted sagittal
:-------------------------:|:-------------------------:
![](./img/4mo/ground_truth/sagittal.png)  |  ![](./img/4mo/inferred/sagittal.png)

Ground-truth axial       |  Predicted axial
:-------------------------:|:-------------------------:
![](./img/4mo/ground_truth/axial.png)  |  ![](./img/4mo/inferred/axial.png)

Dice (foreground): 0.83

### 5 month

Ground-truth coronal       |  Predicted coronal
:-------------------------:|:-------------------------:
![](./img/5mo/ground_truth/coronal.png)  |  ![](./img/5mo/inferred/coronal.png)

Ground-truth sagittal       |  Predicted sagittal
:-------------------------:|:-------------------------:
![](./img/5mo/ground_truth/sagittal.png)  |  ![](./img/5mo/inferred/sagittal.png)

Ground-truth axial       |  Predicted axial
:-------------------------:|:-------------------------:
![](./img/5mo/ground_truth/axial.png)  |  ![](./img/5mo/inferred/axial.png)

Dice (foreground): 0.85

### 6 month

Ground-truth coronal       |  Predicted coronal
:-------------------------:|:-------------------------:
![](./img/6mo/ground_truth/coronal.png)  |  ![](./img/6mo/inferred/coronal.png)

Ground-truth sagittal       |  Predicted sagittal
:-------------------------:|:-------------------------:
![](./img/6mo/ground_truth/sagittal.png)  |  ![](./img/6mo/inferred/sagittal.png)

Ground-truth axial       |  Predicted axial
:-------------------------:|:-------------------------:
![](./img/6mo/ground_truth/axial.png)  |  ![](./img/6mo/inferred/axial.png)

Dice (foreground): 0.90

### 7 month

Ground-truth coronal       |  Predicted coronal
:-------------------------:|:-------------------------:
![](./img/7mo/ground_truth/coronal.png)  |  ![](./img/7mo/inferred/coronal.png)

Ground-truth sagittal       |  Predicted sagittal
:-------------------------:|:-------------------------:
![](./img/7mo/ground_truth/sagittal.png)  |  ![](./img/7mo/inferred/sagittal.png)

Ground-truth axial       |  Predicted axial
:-------------------------:|:-------------------------:
![](./img/7mo/ground_truth/axial.png)  |  ![](./img/7mo/inferred/axial.png)

Dice (foreground): 0.90

### 8 month

Ground-truth coronal       |  Predicted coronal
:-------------------------:|:-------------------------:
![](./img/8mo/ground_truth/coronal.png)  |  ![](./img/8mo/inferred/coronal.png)

Ground-truth sagittal       |  Predicted sagittal
:-------------------------:|:-------------------------:
![](./img/8mo/ground_truth/sagittal.png)  |  ![](./img/8mo/inferred/sagittal.png)

Ground-truth axial       |  Predicted axial
:-------------------------:|:-------------------------:
![](./img/8mo/ground_truth/axial.png)  |  ![](./img/8mo/inferred/axial.png)

Dice (foreground): 0.89
