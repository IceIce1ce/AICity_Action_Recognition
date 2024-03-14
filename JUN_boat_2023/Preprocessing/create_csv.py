import os
import csv
import pandas as pd

cut_videopath = 'Dataset/A1_cut_video'
cut_videoannotation = 'Dataset/A1_cut_video_annotation'
csv_outpath = cut_videopath + '/new_split_by_id_A1_total'
original_zero_csv = csv_outpath + '/original_zero'
expand_zero_csv = csv_outpath + '/expand_zero'
if not os.path.exists(csv_outpath):
    os.makedirs(csv_outpath)
if not os.path.exists(original_zero_csv):
    os.makedirs(original_zero_csv)
if not os.path.exists(expand_zero_csv):
    os.makedirs(expand_zero_csv)
user_id_list = []

# train with all A1
for folder_name in os.listdir('Dataset/A1'):
    user_id_list.append(folder_name[8:])
user_id_list.sort()
train_id = [i for i in range(25)] # dataset 2022 has 25 folders for training
val_id = [i for i in range(20, 25)]
train_user_id_list = str([user_id_list[i] for i in train_id])
val_user_id_list = str([user_id_list[i] for i in val_id])

k_map = {"dashboard": "Dashboard", "rearview": "Rear", "right": "Right"}
annotation_list = [original_zero_csv, expand_zero_csv]

for annotation in annotation_list:
    for view in ["dashboard", "rearview", "right"]:
          if 'expand' in annotation:
            f = open(cut_videoannotation + "/A1_cutvideo_expandzero_total_data.csv", "r")
          else:
            f = open(cut_videoannotation + "/A1_cutvideo_originalzero_total_data.csv", "r")
          f_train = open(annotation + "/train_{}.csv".format(view), "w")
          f_val = open(annotation + "/val_{}.csv".format(view), "w")
          f_test = open(annotation + "/test_{}.csv".format(view), "w")
          for line in f.readlines():
              if line.split('user_id_')[1].split('_NoAudio')[0] in val_user_id_list and k_map[view] in line:
                  f_val.write(line)
                  f_test.write(line)
              elif line.split('user_id_')[1].split('_NoAudio')[0] in train_user_id_list and k_map[view] in line:
                  f_train.write(line)
          f_train.close()
          f_val.close()
  
    for csvtype in ['train', 'val']:
        data1 = []
        with open(annotation + '/{}_dashboard.csv'.format(csvtype), newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                data1.append(row)
        data2 = []
        with open(annotation + '/{}_rearview.csv'.format(csvtype), newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                data2.append(row)
        data3 = []
        with open(annotation +'/{}_right.csv'.format(csvtype), newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                data3.append(row)
        df = pd.concat([pd.DataFrame(data1), pd.DataFrame(data2), pd.DataFrame(data3)])
        df.to_csv(annotation + '/{}_all.csv'.format(csvtype), index=False, header=False)