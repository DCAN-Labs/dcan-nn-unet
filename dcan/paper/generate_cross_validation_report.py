import os.path

from jinja2 import Environment, PackageLoader, select_autoescape

from dcan.evaluation.calculate_dice_for_folder import calculate_dice_for_folder

env = Environment(
    loader=PackageLoader("dcan.paper"),
    autoescape=select_autoescape()
)

template = env.get_template("10FoldValidationResults.md")

data = {}
segmentations_root_folder = '/home/feczk001/shared/data/nnUNet/segmentations/inferred/PaperCrossValidation/'
segmentations_folders = ['Task{}_Paper_Fold{}'.format(516 + i, i) for i in range(10)]
gt_folder = '/home/feczk001/shared/data/nnUNet/raw_data/Task516_525/'
for segmentation_folder in segmentations_folders:
    inferred_fldr = os.path.join(segmentations_root_folder, segmentation_folder)
    dice_scores = calculate_dice_for_folder(gt_folder, inferred_fldr)
    if dice_scores:
        data[inferred_fldr] = dice_scores

print(template.render(dict_item=data))
