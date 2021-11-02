import pandas as pd
import sys


def create_means_contralateral_average(input_file, output_file):
    all_df = pd.read_csv(input_file)

    df = pd.DataFrame(columns=('segment_name', 'Dice'))
    new_row_index = 0
    for i in range(len(all_df.index)):
        row = all_df.loc[i]
        segment_name = row['segment_name']
        dice = float(row['Dice'])
        if segment_name.startswith('Left'):
            base_name = segment_name[5:]
            rhs_name = 'Right-' + base_name
            rhs_row = all_df.loc[(all_df['segment_name'] == rhs_name)].iloc[0]
            rhs_dice = float(rhs_row['Dice'])
            avg_dice = (dice + rhs_dice) / 2.0
            df.loc[new_row_index] = [base_name, avg_dice]
            new_row_index += 1
        elif not segment_name.startswith('Right'):
            df.loc[new_row_index] = [segment_name, dice]
            new_row_index += 1

    df.to_csv(output_file, index=False)


if __name__ == '__main__':
    create_means_contralateral_average(sys.argv[1], sys.argv[2])
