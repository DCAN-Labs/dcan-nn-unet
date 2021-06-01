import os

import nibabel as nib


def dice_coefficient(y_true, y_pred, smooth=1):
    val_to_count = {}
    intersection = 0
    for i in range(117):
        for j in range(159):
            for k in range(126):
                y_true_val = int(y_true[i][j][k])
                if y_true_val not in val_to_count:
                    val_to_count[y_true_val] = 1
                else:
                    val_to_count[y_true_val] = val_to_count[y_true_val] + 1
                y_pred_val = int(y_pred[i][j][k])
                if y_true_val == y_pred_val:
                    intersection += 1
    union = 2. * 117 * 159 * 126
    dice = (2. * intersection + smooth) / (union + smooth)
    all_values = val_to_count.values()
    print(val_to_count)
    max_value = max(all_values)
    guess = max_value / (117 * 159 * 126)
    print(guess)
    return dice


def dice_coef_not_unknown(y_true, y_pred, smooth=1):
    intersection = 0
    union = 0
    for i in range(117):
        for j in range(159):
            for k in range(126):
                y_true_val = int(y_true[i][j][k])
                y_pred_val = int(y_pred[i][j][k])
                if y_true_val != 0 or y_pred_val != 0:
                    union += 1
                    if y_true_val == y_pred_val:
                        intersection += 1
    union = 2. * union
    dice = (2. * intersection + smooth) / (union + smooth)
    return dice


home = '/home/miran045/reine097/'
predictions_filename = os.path.join(home, 'nnUNet/inference/babies/', '00-02mos_Template05.nii.gz')
ground_truth_filename = os.path.join(home, 'nnUNet_raw_data_base/nnUNet_raw_data/Task102_BabiesSubset/test/labelsTest/',
                                     '00-02mos_Template05.nii.gz')

predictions_img = nib.load(predictions_filename)
predictions_data = predictions_img.get_fdata()
print('predictions_data.shape:', predictions_data.shape)
print('predictions_data.dtype', predictions_data.dtype)

gt_img = nib.load(ground_truth_filename)
gt_data = gt_img.get_fdata()
print('gt_data.shape:', gt_data.shape)
print('gt_img.dtype', gt_data.dtype)

print('dice (all):', dice_coefficient(gt_data, predictions_data))

print('dice (not unknown):', dice_coef_not_unknown(gt_data, predictions_data))
