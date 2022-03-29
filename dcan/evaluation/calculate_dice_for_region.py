# Author: Paul Reiners

import sys

import nibabel as nib


def dice_coefficient(y_true, y_pred, region, smooth=1):
    m = 0
    n = 0
    intersection = 0
    max_x = y_true.shape[0]
    max_y = y_true.shape[1]
    max_z = y_true.shape[2]
    for i in range(max_x):
        for j in range(max_y):
            for k in range(max_z):
                y_true_val = int(y_true[i][j][k])
                y_pred_val = int(y_pred[i][j][k])
                if y_true_val == y_pred_val == region:
                    intersection += 1
                if y_true_val == region:
                    m += 1
                if y_pred_val == region:
                    n += 1
    dice = (2. * intersection + smooth) / (m + n + smooth)

    return dice


def calculate_dice_coefficient(gt_filename, preds_filename, region):
    predictions_img = nib.load(preds_filename)
    predictions_data = predictions_img.get_fdata()

    gt_img = nib.load(gt_filename)
    gt_data = gt_img.get_fdata()

    assert predictions_data.shape == gt_data.shape

    return dice_coefficient(gt_data, predictions_data, region)


def main(gt_filename, preds_filename, region):
    return calculate_dice_coefficient(gt_filename, preds_filename, region)


if __name__ == "__main__":
    ground_truth_filename = sys.argv[1]
    predictions_filename = sys.argv[2]
    rgn = int(sys.argv[3])
    result = main(ground_truth_filename, predictions_filename, rgn)
    print('Dice coefficient: ', result)
