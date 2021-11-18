import nibabel as nib
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt


ground_truth_file = '/home/feczk001/shared/data/nnUNet/labelsTs/Task512/8mo_sub-890518.nii.gz'
inferred_file = '/home/feczk001/shared/data/nnUNet/segmentations/inferred/Task512_BCP_ABCD_Neonates_SynthSegDownsample/original/8mo_sub-890518.nii.gz'

predictions_img = nib.load(inferred_file)
predictions_data = predictions_img.get_fdata()

gt_img = nib.load(ground_truth_file)
gt_data = gt_img.get_fdata()

assert predictions_data.shape == gt_data.shape
predictions = []
truth = []
max_x = gt_data.shape[0]
max_y = gt_data.shape[1]
max_z = gt_data.shape[2]
for i in range(max_x):
    for j in range(max_y):
        for k in range(max_z):
            y_true_val = int(gt_data[i][j][k])
            if y_true_val == 0:
                continue
            truth.append(y_true_val)
            y_pred_val = int(predictions_data[i][j][k])
            predictions.append(y_pred_val)

data = {'y_Actual':    truth,
        'y_Predicted': predictions
        }

df = pd.DataFrame(data, columns=['y_Actual','y_Predicted'])
print(df.head())
confusion_matrix = pd.crosstab(df['y_Actual'], df['y_Predicted'], rownames=['Actual'], colnames=['Predicted'])

sn.heatmap(confusion_matrix, annot=False)
plt.show()
