import pandas as pd
import os

def getData(fpath, names=None, sep='\s+|\t+|,'):
    try:
        df = pd.read_csv(fpath, sep=sep, index_col=None, skipinitialspace=True, header=None, names=names, engine='python')
        return df.sort_values(by=df.columns[0:3].tolist(), ascending=[True, True, True])
    except Exception as e:
        raise ValueError("Could not read input from %s. Error: %s" % (os.path.basename(fpath), repr(e)))

labels = getData('refine_A2_submission_0.33.txt', names=['video_id', 'activity_id', 'ts_start', 'ts_end'])
labels = labels.sort_values(by=['video_id', 'ts_start'])
# labels['ts_start'] = labels['ts_start'] - 2
# labels['ts_end'] = labels['ts_end'] + 2

# condition = labels['ts_end'] - labels['ts_start'] > 3
# labels.loc[condition, 'ts_start'] = labels.loc[condition, 'ts_start'] + 1
# labels.loc[condition, 'ts_end'] = labels.loc[condition, 'ts_end'] - 1
labels.to_csv('sort_submission.txt', sep=' ', index=False, header=False)
