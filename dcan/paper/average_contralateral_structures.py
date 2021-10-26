import pandas as pd

input_file = '../../doc/tasks/509/means.csv'
output_file = '../../doc/tasks/509/means_contralateral_average.csv'

means_df = pd.read_csv(input_file)
print(means_df.head())

df = pd.DataFrame(columns=('segment_name', 'Dice'))
for i in range(len(means_df.index)):
    row = means_df.loc[i]
    segment_name = row['segment_name']
    if segment_name.startswith('Left'):
        base_name = segment_name[6:]
        rhs_name = 'Right-' + base_name
        avg_dice = (float(row['Dice']) + )
    df.loc[i] = [i, i + 1]

