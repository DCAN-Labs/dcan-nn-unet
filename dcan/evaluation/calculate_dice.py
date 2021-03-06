# Author: Paul Reiners

import sys

import nibabel as nib


def dice_coefficient(y_true, y_pred, smooth=1):
    val_to_count = {}
    intersection = 0
    max_x = y_true.shape[0]
    max_y = y_true.shape[1]
    max_z = y_true.shape[2]
    for i in range(max_x):
        for j in range(max_y):
            for k in range(max_z):
                y_true_val = int(y_true[i][j][k])
                if y_true_val not in val_to_count:
                    val_to_count[y_true_val] = 1
                else:
                    val_to_count[y_true_val] = val_to_count[y_true_val] + 1
                y_pred_val = int(y_pred[i][j][k])
                if y_true_val == y_pred_val:
                    intersection += 1
    union = 2. * max_x * max_y * max_z
    dice = (2. * intersection + smooth) / (union + smooth)
    all_values = val_to_count.values()
    print(val_to_count)
    max_value = max(all_values)
    guess = max_value / (max_x * max_y * max_z)
    print(guess)
    return dice


def dice_coef_not_unknown(y_true, y_pred, smooth=1):
    intersection = 0
    union = 0
    max_x = y_true.shape[0]
    max_y = y_true.shape[1]
    max_z = y_true.shape[2]
    for i in range(max_x):
        for j in range(max_y):
            for k in range(max_z):
                y_true_val = int(y_true[i][j][k])
                y_pred_val = int(y_pred[i][j][k])
                if y_true_val != 0:
                    union += 1
                    if y_true_val == y_pred_val:
                        intersection += 1
    union = 2. * union
    dice = (2. * intersection + smooth) / (union + smooth)
    return dice


def calculate_dice_coefficient(gt_filename, preds_filename):
    predictions_img = nib.load(preds_filename)
    predictions_data = predictions_img.get_fdata()

    gt_img = nib.load(gt_filename)
    gt_data = gt_img.get_fdata()

    assert predictions_data.shape == gt_data.shape

    return dice_coef_not_unknown(gt_data, predictions_data)


def main(gt_filename, preds_filename):
    return calculate_dice_coefficient(gt_filename, preds_filename)


if __name__ == "__main__":
    ground_truth_filename = sys.argv[1]
    predictions_filename = sys.argv[2]
    result = main(ground_truth_filename, predictions_filename)
    print('Dice coefficient: ', result)
