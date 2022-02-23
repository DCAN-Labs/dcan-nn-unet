import os.path

import pandas as pd
import matplotlib.pyplot as plt

data = {}
results_dir = '/home/feczk001/shared/data/nnUNet/segmentations/inferred/PaperCrossValidation/results/'
folds = ['fold{}'.format(i) for i in range(10)]
frames = []
for fold in folds:
    data_file_path = os.path.join(results_dir, fold, 'hausdorff', 'hausdorff.csv')
    if os.path.exists(data_file_path):
        hausdorff_data = pd.read_csv(data_file_path)
        frames.append(hausdorff_data)
all_hausdorff_data = pd.concat(frames, axis=0)
print(all_hausdorff_data.columns)
all_hausdorff_data['age_in_months'] = all_hausdorff_data.apply(lambda row: int(row['subject'][0][:1]), axis=1)
all_hausdorff_data.drop(['subject'], axis=1, inplace=True)
hausdorff_means = all_hausdorff_data.groupby('age_in_months').mean()
plt.figure(); hausdorff_means.plot(); plt.legend(loc='best')
print(hausdorff_means.head())
