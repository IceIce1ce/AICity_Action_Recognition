import pandas as pd
import numpy as np

df = pd.read_csv('refine_A2_submission_0.33.txt', delimiter=' ', names=["ID", "Label (Primary)", "Start Time", "End Time"])
df = df.sort_values(by=['ID', 'Start Time'])
# condition1 = df['Label (Primary)'] == 1
# condition2 = df['Label (Primary)'] == 2
# condition3 = df['Label (Primary)'] == 3
# condition4 = df['Label (Primary)'] == 4
# condition5 = df['Label (Primary)'] == 5
# condition6 = df['Label (Primary)'] == 6
# condition7 = df['Label (Primary)'] == 7
# condition8 = df['Label (Primary)'] == 8
# condition9 = df['Label (Primary)'] == 9
# condition10 = df['Label (Primary)'] == 10
# condition11 = df['Label (Primary)'] == 11
# condition12 = df['Label (Primary)'] == 12
# condition13 = df['Label (Primary)'] == 13
# condition14 = df['Label (Primary)'] == 14
# condition15 = df['Label (Primary)'] == 15
# df.loc[condition1, 'End Time'] = df.loc[condition1, 'End Time'] + 1
# df.loc[condition4, 'End Time'] = df.loc[condition4, 'End Time'] - 6
# df.loc[condition5, 'End Time'] = df.loc[condition5, 'End Time'] - 1
# df.loc[condition7, 'End Time'] = df.loc[condition7, 'End Time'] - 1
# df.loc[condition8, 'End Time'] = df.loc[condition8, 'End Time'] - 1
# df.loc[condition9, 'End Time'] = df.loc[condition9, 'End Time'] - 1
# df.loc[condition10, 'End Time'] = df.loc[condition10, 'End Time'] + 1
# df.loc[condition12, 'End Time'] = df.loc[condition12, 'End Time'] - 1
# df.loc[condition13, 'End Time'] = df.loc[condition13, 'End Time'] - 3
# df.loc[condition14, 'End Time'] = df.loc[condition14, 'End Time'] - 2

df['Time Difference'] = df['End Time'] - df['Start Time']
list_mean = []
list_median = []
list_max = []
list_min = []
list_std = []
for i in range(1, 16):
	list_mean.append(df[df['Label (Primary)'] == i]['Time Difference'].mean())
	list_median.append(df[df['Label (Primary)'] == i]['Time Difference'].median())
	list_max.append(df[df['Label (Primary)'] == i]['Time Difference'].max())
	list_min.append(df[df['Label (Primary)'] == i]['Time Difference'].min())
	list_std.append(df[df['Label (Primary)'] == i]['Time Difference'].std())
dict = {'Class': np.arange(1, 16), 'Mean': list_mean, 'Median': list_median, 'Max': list_max, 'Min': list_min, 'Std': list_std}
final_df = pd.DataFrame(dict)
print(final_df)

# df.to_csv('fix_my_submission.txt', sep=' ', index=False, header=False)