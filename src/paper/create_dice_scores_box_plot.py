# Author: Paul Reiners

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys


def create_dice_scores_box_plot(input_file, output_file):
    all_df = pd.read_csv(input_file)

    df = pd.DataFrame(columns=('reference', 'segment_name', 'Dice'))
    new_row_index = 0
    for i in range(len(all_df.index)):
        row = all_df.loc[i]
        segment_name = row['segment_name']
        reference = row['reference']
        dice = float(row['Dice'])
        if segment_name.startswith('Left'):
            base_name = segment_name[5:]
            rhs_name = 'Right-' + base_name
            rhs_row = all_df.loc[(all_df['segment_name'] == rhs_name) & (reference == row['reference'])].iloc[0]
            rhs_dice = float(rhs_row['Dice'])
            avg_dice = (dice + rhs_dice) / 2.0
            df.loc[new_row_index] = [reference, base_name, avg_dice]
            new_row_index += 1
        elif not segment_name.startswith('Right'):
            df.loc[new_row_index] = [reference, segment_name, dice]
            new_row_index += 1

    print(df.segment_name.unique())

    segment_names_to_abbreviations = \
        {'Cerebral-Cortex': 'CT', 'Cerebral-White-Matter': 'WM', 'Lateral-Ventricle': 'LV', 'Cerebellum-Cortex': 'CC',
         'Thalamus-Proper*': 'TH', 'Caudate': 'CA', 'Putamen': 'P', 'Pallidum': 'PA',
         'Brain-Stem': 'BS', 'Hippocampus': 'HP', 'Amygdala': 'AM'}

    data = \
        [np.asarray(df.loc[(df['segment_name'] == segment_name)]['Dice'].tolist()) for segment_name in
         segment_names_to_abbreviations.keys()]

    fig, axs = plt.subplots(1, 1)

    # basic plot
    axs.boxplot(data)
    axs.set_title('Dice scores')

    axs.set_xticklabels(segment_names_to_abbreviations.values())
    plt.savefig(output_file)

    plt.show()


if __name__ == '__main__':
    create_dice_scores_box_plot(sys.argv[1], sys.argv[2])
