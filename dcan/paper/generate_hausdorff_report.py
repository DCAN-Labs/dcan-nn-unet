import os.path

import numpy as np
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader("dcan.paper"),
    autoescape=select_autoescape()
)

template = env.get_template("HausdorffResults.md")

data = {}
results_dir = '/home/feczk001/shared/data/nnUNet/segmentations/inferred/PaperCrossValidation/results/'
folds = ['fold{}'.format(i) for i in range(10)]
existing_folds = []
fold = 'fold0'
data_file_path = os.path.join(results_dir, fold, 'hausdorff', 'hausdorff.npy')
if os.path.exists(data_file_path):
    existing_folds.append(fold)
    labels_file_path = os.path.join(results_dir, fold, 'labels.txt')
    with open(labels_file_path) as fp:
        lines = fp.readlines()
        labels = [int(line.strip()) for line in lines]
        data['labels'] = labels
    path_segs_path = os.path.join(results_dir, fold, 'path_segs.txt')
    with open(path_segs_path) as fp:
        lines = fp.readlines()
        paths_segs = [line.strip() for line in lines]
        data['paths_segs'] = paths_segs
    hausdorff_data = np.load(data_file_path)
    data['hausdorff_data'] = hausdorff_data
    data['existing_folds'] = existing_folds

output = template.render(dict_item=data)
print(output)
