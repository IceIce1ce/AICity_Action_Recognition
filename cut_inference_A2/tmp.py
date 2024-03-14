import pandas as pd

def seconds_to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, remaining_seconds)

list_start1, list_end1, list_action1 = [], [], []
list_start2, list_end2, list_action2 = [], [], []
list_start3, list_end3, list_action3 = [], [], []
list_start4, list_end4, list_action4 = [], [], []
list_start5, list_end5, list_action5 = [], [], []
list_start6, list_end6, list_action6 = [], [], []
list_start7, list_end7, list_action7 = [], [], []
list_start8, list_end8, list_action8 = [], [], []
list_start9, list_end9, list_action9 = [], [], []
list_start10, list_end10, list_action10 = [], [], []
list_start11, list_end11, list_action11 = [], [], []
list_start12, list_end12, list_action12 = [], [], []
list_start13, list_end13, list_action13 = [], [], []
list_start14, list_end14, list_action14 = [], [], []
list_start15, list_end15, list_action15 = [], [], []
list_start16, list_end16, list_action16 = [], [], []
list_start17, list_end17, list_action17 = [], [], []
list_start18, list_end18, list_action18 = [], [], []
list_start19, list_end19, list_action19 = [], [], []
list_start20, list_end20, list_action20 = [], [], []
list_start21, list_end21, list_action21 = [], [], []
list_start22, list_end22, list_action22 = [], [], []
list_start23, list_end23, list_action23 = [], [], []
list_start24, list_end24, list_action24 = [], [], []
list_start25, list_end25, list_action25 = [], [], []
list_start26, list_end26, list_action26 = [], [], []
list_start27, list_end27, list_action27 = [], [], []
list_start28, list_end28, list_action28 = [], [], []
list_start29, list_end29, list_action29 = [], [], []
list_start30, list_end30, list_action30 = [], [], []

with open('my_submission.txt', 'r') as f:
    for line in f:
        data = line.strip().split(' ')
        user_id, action, start, end = int(data[0]), int(data[1]), int(data[2]), int(data[3])
        if user_id == 1:
            list_action1.append(action)
            list_start1.append(start)
            list_end1.append(end)
        elif user_id == 2:
            list_action2.append(action)
            list_start2.append(start)
            list_end2.append(end)
        elif user_id == 3:
            list_action3.append(action)
            list_start3.append(start)
            list_end3.append(end)
        elif user_id == 4:
            list_action4.append(action)
            list_start4.append(start)
            list_end4.append(end)
        elif user_id == 5:
            list_action5.append(action)
            list_start5.append(start)
            list_end5.append(end)
        elif user_id == 6:
            list_action6.append(action)
            list_start6.append(start)
            list_end6.append(end)
        elif user_id == 7:
            list_action7.append(action)
            list_start7.append(start)
            list_end7.append(end)
        elif user_id == 8:
            list_action8.append(action)
            list_start8.append(start)
            list_end8.append(end)
        elif user_id == 9:
            list_action9.append(action)
            list_start9.append(start)
            list_end9.append(end)
        elif user_id == 10:
            list_action10.append(action)
            list_start10.append(start)
            list_end10.append(end)
        elif user_id == 11:
            list_action11.append(action)
            list_start11.append(start)
            list_end11.append(end)
        elif user_id == 12:
            list_action12.append(action)
            list_start12.append(start)
            list_end12.append(end)
        elif user_id == 13:
            list_action13.append(action)
            list_start13.append(start)
            list_end13.append(end)
        elif user_id == 14:
            list_action14.append(action)
            list_start14.append(start)
            list_end14.append(end)
        elif user_id == 15:
            list_action15.append(action)
            list_start15.append(start)
            list_end15.append(end)
        elif user_id == 16:
            list_action16.append(action)
            list_start16.append(start)
            list_end16.append(end)
        elif user_id == 17:
            list_action17.append(action)
            list_start17.append(start)
            list_end17.append(end)
        elif user_id == 18:
            list_action18.append(action)
            list_start18.append(start)
            list_end18.append(end)
        elif user_id == 19:
            list_action19.append(action)
            list_start19.append(start)
            list_end19.append(end)
        elif user_id == 20:
            list_action20.append(action)
            list_start20.append(start)
            list_end20.append(end)
        elif user_id == 21:
            list_action21.append(action)
            list_start21.append(start)
            list_end21.append(end)
        elif user_id == 22:
            list_action22.append(action)
            list_start22.append(start)
            list_end22.append(end)
        elif user_id == 23:
            list_action23.append(action)
            list_start23.append(start)
            list_end23.append(end)
        elif user_id == 24:
            list_action24.append(action)
            list_start24.append(start)
            list_end24.append(end)
        elif user_id == 25:
            list_action25.append(action)
            list_start25.append(start)
            list_end25.append(end)
        elif user_id == 26:
            list_action26.append(action)
            list_start26.append(start)
            list_end26.append(end)
        elif user_id == 27:
            list_action27.append(action)
            list_start27.append(start)
            list_end27.append(end)
        elif user_id == 28:
            list_action28.append(action)
            list_start28.append(start)
            list_end28.append(end)
        elif user_id == 29:
            list_action29.append(action)
            list_start29.append(start)
            list_end29.append(end)
        elif user_id == 30:
            list_action30.append(action)
            list_start30.append(start)
            list_end30.append(end)

for i in range(len(list_start1)):
    list_start1[i] = seconds_to_time(list_start1[i])
    list_end1[i] = seconds_to_time(list_end1[i])
    list_action1[i] = 'Class ' + str(list_action1[i])
for i in range(len(list_start2)):
    list_start2[i] = seconds_to_time(list_start2[i])
    list_end2[i] = seconds_to_time(list_end2[i])
    list_action2[i] = 'Class ' + str(list_action2[i])
df1a = pd.DataFrame({'Filename': 'Dashboard_user_id_12670_5', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start1, 'End Time': list_end1, 'Label (Primary)': list_action1, 'Appearance Block': 'None'})
df1b = pd.DataFrame({'Filename': 'Dashboard_user_id_12670_7', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start2, 'End Time': list_end2, 'Label (Primary)': list_action2, 'Appearance Block': 'None'})
df1c = pd.DataFrame({'Filename': 'Rear_view_user_id_12670_5', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start1, 'End Time': list_end1, 'Label (Primary)': list_action1, 'Appearance Block': 'None'})
df1d = pd.DataFrame({'Filename': 'Rear_view_user_id_12670_7', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start2, 'End Time': list_end2, 'Label (Primary)': list_action2, 'Appearance Block': 'None'})
df1e = pd.DataFrame({'Filename': 'Right_side_window_user_id_12670_5', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start1, 'End Time': list_end1, 'Label (Primary)': list_action1, 'Appearance Block': 'None'})
df1f = pd.DataFrame({'Filename': 'Right_side_window_user_id_12670_7', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start2, 'End Time': list_end2, 'Label (Primary)': list_action2, 'Appearance Block': 'None'})
df1 = pd.concat([df1a, df1b, df1c, df1d, df1e, df1f])
df1.to_csv('user_id_12670.csv', header=True, index=False)

for i in range(len(list_start3)):
    list_start3[i] = seconds_to_time(list_start3[i])
    list_end3[i] = seconds_to_time(list_end3[i])
    list_action3[i] = 'Class ' + str(list_action3[i])
for i in range(len(list_start4)):
    list_start4[i] = seconds_to_time(list_start4[i])
    list_end4[i] = seconds_to_time(list_end4[i])
    list_action4[i] = 'Class ' + str(list_action4[i])
df2a = pd.DataFrame({'Filename': 'Dashboard_user_id_13148_5', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start3, 'End Time': list_end3, 'Label (Primary)': list_action3, 'Appearance Block': 'None'})
df2b = pd.DataFrame({'Filename': 'Dashboard_user_id_13148_7', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start4, 'End Time': list_end4, 'Label (Primary)': list_action4, 'Appearance Block': 'None'})
df2c = pd.DataFrame({'Filename': 'Rear_view_user_id_13148_5', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start3, 'End Time': list_end3, 'Label (Primary)': list_action3, 'Appearance Block': 'None'})
df2d = pd.DataFrame({'Filename': 'Rear_view_user_id_13148_7', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start4, 'End Time': list_end4, 'Label (Primary)': list_action4, 'Appearance Block': 'None'})
df2e = pd.DataFrame({'Filename': 'Right_side_window_user_id_13148_5', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start3, 'End Time': list_end3, 'Label (Primary)': list_action3, 'Appearance Block': 'None'})
df2f = pd.DataFrame({'Filename': 'Right_side_window_user_id_13148_7', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start4, 'End Time': list_end4, 'Label (Primary)': list_action4, 'Appearance Block': 'None'})
df2 = pd.concat([df2a, df2b, df2c, df2d, df2e, df2f])
df2.to_csv('user_id_13148.csv', header=True, index=False)

for i in range(len(list_start5)):
    list_start5[i] = seconds_to_time(list_start5[i])
    list_end5[i] = seconds_to_time(list_end5[i])
    list_action5[i] = 'Class ' + str(list_action5[i])
for i in range(len(list_start6)):
    list_start6[i] = seconds_to_time(list_start6[i])
    list_end6[i] = seconds_to_time(list_end6[i])
    list_action6[i] = 'Class ' + str(list_action6[i])
df3a = pd.DataFrame({'Filename': 'Dashboard_user_id_15198_5', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start5, 'End Time': list_end5, 'Label (Primary)': list_action5, 'Appearance Block': 'None'})
df3b = pd.DataFrame({'Filename': 'Dashboard_user_id_15198_7', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start6, 'End Time': list_end6, 'Label (Primary)': list_action6, 'Appearance Block': 'None'})
df3c = pd.DataFrame({'Filename': 'Rear_view_user_id_15198_5', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start5, 'End Time': list_end5, 'Label (Primary)': list_action5, 'Appearance Block': 'None'})
df3d = pd.DataFrame({'Filename': 'Rear_view_user_id_15198_7', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start6, 'End Time': list_end6, 'Label (Primary)': list_action6, 'Appearance Block': 'None'})
df3e = pd.DataFrame({'Filename': 'Right_side_window_user_id_15198_5', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start5, 'End Time': list_end5, 'Label (Primary)': list_action5, 'Appearance Block': 'None'})
df3f = pd.DataFrame({'Filename': 'Right_side_window_user_id_15198_7', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start6, 'End Time': list_end6, 'Label (Primary)': list_action6, 'Appearance Block': 'None'})
df3 = pd.concat([df3a, df3b, df3c, df3d, df3e, df3f])
df3.to_csv('user_id_15198.csv', header=True, index=False)

for i in range(len(list_start7)):
    list_start7[i] = seconds_to_time(list_start7[i])
    list_end7[i] = seconds_to_time(list_end7[i])
    list_action7[i] = 'Class ' + str(list_action7[i])
for i in range(len(list_start8)):
    list_start8[i] = seconds_to_time(list_start8[i])
    list_end8[i] = seconds_to_time(list_end8[i])
    list_action8[i] = 'Class ' + str(list_action8[i])
df4a = pd.DataFrame({'Filename': 'Dashboard_user_id_22530_5', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start7, 'End Time': list_end7, 'Label (Primary)': list_action7, 'Appearance Block': 'None'})
df4b = pd.DataFrame({'Filename': 'Dashboard_user_id_22530_7', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start8, 'End Time': list_end8, 'Label (Primary)': list_action8, 'Appearance Block': 'None'})
df4c = pd.DataFrame({'Filename': 'Rear_view_user_id_22530_5', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start7, 'End Time': list_end7, 'Label (Primary)': list_action7, 'Appearance Block': 'None'})
df4d = pd.DataFrame({'Filename': 'Rear_view_user_id_22530_7', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start8, 'End Time': list_end8, 'Label (Primary)': list_action8, 'Appearance Block': 'None'})
df4e = pd.DataFrame({'Filename': 'Right_side_window_user_id_22530_5', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start7, 'End Time': list_end7, 'Label (Primary)': list_action7, 'Appearance Block': 'None'})
df4f = pd.DataFrame({'Filename': 'Right_side_window_user_id_22530_7', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start8, 'End Time': list_end8, 'Label (Primary)': list_action8, 'Appearance Block': 'None'})
df4 = pd.concat([df4a, df4b, df4c, df4d, df4e, df4f])
df4.to_csv('user_id_22530.csv', header=True, index=False)

for i in range(len(list_start9)):
    list_start9[i] = seconds_to_time(list_start9[i])
    list_end9[i] = seconds_to_time(list_end9[i])
    list_action9[i] = 'Class ' + str(list_action9[i])
for i in range(len(list_start10)):
    list_start10[i] = seconds_to_time(list_start10[i])
    list_end10[i] = seconds_to_time(list_end10[i])
    list_action10[i] = 'Class ' + str(list_action10[i])
df5a = pd.DataFrame({'Filename': 'Dashboard_user_id_26223_3', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start9, 'End Time': list_end9, 'Label (Primary)': list_action9, 'Appearance Block': 'None'})
df5b = pd.DataFrame({'Filename': 'Dashboard_user_id_26223_5', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start10, 'End Time': list_end10, 'Label (Primary)': list_action10, 'Appearance Block': 'None'})
df5c = pd.DataFrame({'Filename': 'Rear_view_user_id_26223_3', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start9, 'End Time': list_end9, 'Label (Primary)': list_action9, 'Appearance Block': 'None'})
df5d = pd.DataFrame({'Filename': 'Rear_view_user_id_26223_5', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start10, 'End Time': list_end10, 'Label (Primary)': list_action10, 'Appearance Block': 'None'})
df5e = pd.DataFrame({'Filename': 'Right_side_window_user_id_26223_3', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start9, 'End Time': list_end9, 'Label (Primary)': list_action9, 'Appearance Block': 'None'})
df5f = pd.DataFrame({'Filename': 'Right_side_window_user_id_26223_5', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start10, 'End Time': list_end10, 'Label (Primary)': list_action10, 'Appearance Block': 'None'})
df5 = pd.concat([df5a, df5b, df5c, df5d, df5e, df5f])
df5.to_csv('user_id_26223.csv', header=True, index=False)

for i in range(len(list_start11)):
    list_start11[i] = seconds_to_time(list_start11[i])
    list_end11[i] = seconds_to_time(list_end11[i])
    list_action11[i] = 'Class ' + str(list_action11[i])
for i in range(len(list_start12)):
    list_start12[i] = seconds_to_time(list_start12[i])
    list_end12[i] = seconds_to_time(list_end12[i])
    list_action12[i] = 'Class ' + str(list_action12[i])
df6a = pd.DataFrame({'Filename': 'Dashboard_user_id_33508_5', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start11, 'End Time': list_end11, 'Label (Primary)': list_action11, 'Appearance Block': 'None'})
df6b = pd.DataFrame({'Filename': 'Dashboard_user_id_33508_7', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start12, 'End Time': list_end12, 'Label (Primary)': list_action12, 'Appearance Block': 'None'})
df6c = pd.DataFrame({'Filename': 'Rear_view_user_id_33508_5', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start11, 'End Time': list_end11, 'Label (Primary)': list_action11, 'Appearance Block': 'None'})
df6d = pd.DataFrame({'Filename': 'Rear_view_user_id_33508_7', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start12, 'End Time': list_end12, 'Label (Primary)': list_action12, 'Appearance Block': 'None'})
df6e = pd.DataFrame({'Filename': 'Right_side_window_user_id_33508_5', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start11, 'End Time': list_end11, 'Label (Primary)': list_action11, 'Appearance Block': 'None'})
df6f = pd.DataFrame({'Filename': 'Right_side_window_user_id_33508_7', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start12, 'End Time': list_end12, 'Label (Primary)': list_action12, 'Appearance Block': 'None'})
df6 = pd.concat([df6a, df6b, df6c, df6d, df6e, df6f])
df6.to_csv('user_id_33508.csv', header=True, index=False)

for i in range(len(list_start13)):
    list_start13[i] = seconds_to_time(list_start13[i])
    list_end13[i] = seconds_to_time(list_end13[i])
    list_action13[i] = 'Class ' + str(list_action13[i])
for i in range(len(list_start14)):
    list_start14[i] = seconds_to_time(list_start14[i])
    list_end14[i] = seconds_to_time(list_end14[i])
    list_action14[i] = 'Class ' + str(list_action14[i])
df7a = pd.DataFrame({'Filename': 'Dashboard_user_id_42897_5', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start13, 'End Time': list_end13, 'Label (Primary)': list_action13, 'Appearance Block': 'None'})
df7b = pd.DataFrame({'Filename': 'Dashboard_user_id_42897_7', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start14, 'End Time': list_end14, 'Label (Primary)': list_action14, 'Appearance Block': 'None'})
df7c = pd.DataFrame({'Filename': 'Rear_view_user_id_42897_5', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start13, 'End Time': list_end13, 'Label (Primary)': list_action13, 'Appearance Block': 'None'})
df7d = pd.DataFrame({'Filename': 'Rear_view_user_id_42897_7', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start14, 'End Time': list_end14, 'Label (Primary)': list_action14, 'Appearance Block': 'None'})
df7e = pd.DataFrame({'Filename': 'Right_side_window_user_id_42897_5', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start13, 'End Time': list_end13, 'Label (Primary)': list_action13, 'Appearance Block': 'None'})
df7f = pd.DataFrame({'Filename': 'Right_side_window_user_id_42897_7', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start14, 'End Time': list_end14, 'Label (Primary)': list_action14, 'Appearance Block': 'None'})
df7 = pd.concat([df7a, df7b, df7c, df7d, df7e, df7f])
df7.to_csv('user_id_42897.csv', header=True, index=False)

for i in range(len(list_start15)):
    list_start15[i] = seconds_to_time(list_start15[i])
    list_end15[i] = seconds_to_time(list_end15[i])
    list_action15[i] = 'Class ' + str(list_action15[i])
for i in range(len(list_start16)):
    list_start16[i] = seconds_to_time(list_start16[i])
    list_end16[i] = seconds_to_time(list_end16[i])
    list_action16[i] = 'Class ' + str(list_action16[i])
df8a = pd.DataFrame({'Filename': 'Dashboard_user_id_49989_5', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start15, 'End Time': list_end15, 'Label (Primary)': list_action15, 'Appearance Block': 'None'})
df8b = pd.DataFrame({'Filename': 'Dashboard_user_id_49989_7', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start16, 'End Time': list_end16, 'Label (Primary)': list_action16, 'Appearance Block': 'None'})
df8c = pd.DataFrame({'Filename': 'Rear_view_user_id_49989_5', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start15, 'End Time': list_end15, 'Label (Primary)': list_action15, 'Appearance Block': 'None'})
df8d = pd.DataFrame({'Filename': 'Rear_view_user_id_49989_7', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start16, 'End Time': list_end16, 'Label (Primary)': list_action16, 'Appearance Block': 'None'})
df8e = pd.DataFrame({'Filename': 'Right_side_window_user_id_49989_5', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start15, 'End Time': list_end15, 'Label (Primary)': list_action15, 'Appearance Block': 'None'})
df8f = pd.DataFrame({'Filename': 'Right_side_window_user_id_49989_7', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start16, 'End Time': list_end16, 'Label (Primary)': list_action16, 'Appearance Block': 'None'})
df8 = pd.concat([df8a, df8b, df8c, df8d, df8e, df8f])
df8.to_csv('user_id_49989.csv', header=True, index=False)

for i in range(len(list_start17)):
    list_start17[i] = seconds_to_time(list_start17[i])
    list_end17[i] = seconds_to_time(list_end17[i])
    list_action17[i] = 'Class ' + str(list_action17[i])
for i in range(len(list_start18)):
    list_start18[i] = seconds_to_time(list_start18[i])
    list_end18[i] = seconds_to_time(list_end18[i])
    list_action18[i] = 'Class ' + str(list_action18[i])
df9a = pd.DataFrame({'Filename': 'Dashboard_user_id_51953_3', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start17, 'End Time': list_end17, 'Label (Primary)': list_action17, 'Appearance Block': 'None'})
df9b = pd.DataFrame({'Filename': 'Dashboard_user_id_51953_7', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start18, 'End Time': list_end18, 'Label (Primary)': list_action18, 'Appearance Block': 'None'})
df9c = pd.DataFrame({'Filename': 'Rear_view_user_id_51953_3', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start17, 'End Time': list_end17, 'Label (Primary)': list_action17, 'Appearance Block': 'None'})
df9d = pd.DataFrame({'Filename': 'Rear_view_user_id_51953_7', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start18, 'End Time': list_end18, 'Label (Primary)': list_action18, 'Appearance Block': 'None'})
df9e = pd.DataFrame({'Filename': 'Right_side_window_user_id_51953_3', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start17, 'End Time': list_end17, 'Label (Primary)': list_action17, 'Appearance Block': 'None'})
df9f = pd.DataFrame({'Filename': 'Right_side_window_user_id_51953_7', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start18, 'End Time': list_end18, 'Label (Primary)': list_action18, 'Appearance Block': 'None'})
df9 = pd.concat([df9a, df9b, df9c, df9d, df9e, df9f])
df9.to_csv('user_id_51953.csv', header=True, index=False)

for i in range(len(list_start19)):
    list_start19[i] = seconds_to_time(list_start19[i])
    list_end19[i] = seconds_to_time(list_end19[i])
    list_action19[i] = 'Class ' + str(list_action19[i])
for i in range(len(list_start20)):
    list_start20[i] = seconds_to_time(list_start20[i])
    list_end20[i] = seconds_to_time(list_end20[i])
    list_action20[i] = 'Class ' + str(list_action20[i])
df10a = pd.DataFrame({'Filename': 'Dashboard_user_id_65840_5', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start19, 'End Time': list_end19, 'Label (Primary)': list_action19, 'Appearance Block': 'None'})
df10b = pd.DataFrame({'Filename': 'Dashboard_user_id_65840_7', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start20, 'End Time': list_end20, 'Label (Primary)': list_action20, 'Appearance Block': 'None'})
df10c = pd.DataFrame({'Filename': 'Rear_view_user_id_65840_5', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start19, 'End Time': list_end19, 'Label (Primary)': list_action19, 'Appearance Block': 'None'})
df10d = pd.DataFrame({'Filename': 'Rear_view_user_id_65840_7', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start20, 'End Time': list_end20, 'Label (Primary)': list_action20, 'Appearance Block': 'None'})
df10e = pd.DataFrame({'Filename': 'Right_side_window_user_id_65840_5', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start19, 'End Time': list_end19, 'Label (Primary)': list_action19, 'Appearance Block': 'None'})
df10f = pd.DataFrame({'Filename': 'Right_side_window_user_id_65840_7', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start20, 'End Time': list_end20, 'Label (Primary)': list_action20, 'Appearance Block': 'None'})
df10 = pd.concat([df10a, df10b, df10c, df10d, df10e, df10f])
df10.to_csv('user_id_65840.csv', header=True, index=False)

for i in range(len(list_start21)):
    list_start21[i] = seconds_to_time(list_start21[i])
    list_end21[i] = seconds_to_time(list_end21[i])
    list_action21[i] = 'Class ' + str(list_action21[i])
for i in range(len(list_start22)):
    list_start22[i] = seconds_to_time(list_start22[i])
    list_end22[i] = seconds_to_time(list_end22[i])
    list_action22[i] = 'Class ' + str(list_action22[i])
df11a = pd.DataFrame({'Filename': 'Dashboard_user_id_78826_5', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start21, 'End Time': list_end21, 'Label (Primary)': list_action21, 'Appearance Block': 'None'})
df11b = pd.DataFrame({'Filename': 'Dashboard_user_id_78826_7', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start22, 'End Time': list_end22, 'Label (Primary)': list_action22, 'Appearance Block': 'None'})
df11c = pd.DataFrame({'Filename': 'Rear_view_user_id_78826_5', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start21, 'End Time': list_end21, 'Label (Primary)': list_action21, 'Appearance Block': 'None'})
df11d = pd.DataFrame({'Filename': 'Rear_view_user_id_78826_7', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start22, 'End Time': list_end22, 'Label (Primary)': list_action22, 'Appearance Block': 'None'})
df11e = pd.DataFrame({'Filename': 'Right_side_window_user_id_78826_5', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start21, 'End Time': list_end21, 'Label (Primary)': list_action21, 'Appearance Block': 'None'})
df11f = pd.DataFrame({'Filename': 'Right_side_window_user_id_78826_7', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start22, 'End Time': list_end22, 'Label (Primary)': list_action22, 'Appearance Block': 'None'})
df11 = pd.concat([df11a, df11b, df11c, df11d, df11e, df11f])
df11.to_csv('user_id_78826.csv', header=True, index=False)

for i in range(len(list_start23)):
    list_start23[i] = seconds_to_time(list_start23[i])
    list_end23[i] = seconds_to_time(list_end23[i])
    list_action23[i] = 'Class ' + str(list_action23[i])
for i in range(len(list_start24)):
    list_start24[i] = seconds_to_time(list_start24[i])
    list_end24[i] = seconds_to_time(list_end24[i])
    list_action24[i] = 'Class ' + str(list_action24[i])
df12a = pd.DataFrame({'Filename': 'Dashboard_user_id_81902_5', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start23, 'End Time': list_end23, 'Label (Primary)': list_action23, 'Appearance Block': 'None'})
df12b = pd.DataFrame({'Filename': 'Dashboard_user_id_81902_7', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start24, 'End Time': list_end24, 'Label (Primary)': list_action24, 'Appearance Block': 'None'})
df12c = pd.DataFrame({'Filename': 'Rear_view_user_id_81902_5', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start23, 'End Time': list_end23, 'Label (Primary)': list_action23, 'Appearance Block': 'None'})
df12d = pd.DataFrame({'Filename': 'Rear_view_user_id_81902_7', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start24, 'End Time': list_end24, 'Label (Primary)': list_action24, 'Appearance Block': 'None'})
df12e = pd.DataFrame({'Filename': 'Right_side_window_user_id_81902_5', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start23, 'End Time': list_end23, 'Label (Primary)': list_action23, 'Appearance Block': 'None'})
df12f = pd.DataFrame({'Filename': 'Right_side_window_user_id_81902_7', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start24, 'End Time': list_end24, 'Label (Primary)': list_action24, 'Appearance Block': 'None'})
df12 = pd.concat([df12a, df12b, df12c, df12d, df12e, df12f])
df12.to_csv('user_id_81902.csv', header=True, index=False)

for i in range(len(list_start25)):
    list_start25[i] = seconds_to_time(list_start25[i])
    list_end25[i] = seconds_to_time(list_end25[i])
    list_action25[i] = 'Class ' + str(list_action25[i])
for i in range(len(list_start26)):
    list_start26[i] = seconds_to_time(list_start26[i])
    list_end26[i] = seconds_to_time(list_end26[i])
    list_action26[i] = 'Class ' + str(list_action26[i])
df13a = pd.DataFrame({'Filename': 'Dashboard_user_id_87837_5', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start25, 'End Time': list_end25, 'Label (Primary)': list_action25, 'Appearance Block': 'None'})
df13b = pd.DataFrame({'Filename': 'Dashboard_user_id_87837_7', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start26, 'End Time': list_end26, 'Label (Primary)': list_action26, 'Appearance Block': 'None'})
df13c = pd.DataFrame({'Filename': 'Rear_view_user_id_87837_5', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start25, 'End Time': list_end25, 'Label (Primary)': list_action25, 'Appearance Block': 'None'})
df13d = pd.DataFrame({'Filename': 'Rear_view_user_id_87837_7', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start26, 'End Time': list_end26, 'Label (Primary)': list_action26, 'Appearance Block': 'None'})
df13e = pd.DataFrame({'Filename': 'Right_side_window_user_id_87837_5', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start25, 'End Time': list_end25, 'Label (Primary)': list_action25, 'Appearance Block': 'None'})
df13f = pd.DataFrame({'Filename': 'Right_side_window_user_id_87837_7', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start26, 'End Time': list_end26, 'Label (Primary)': list_action26, 'Appearance Block': 'None'})
df13 = pd.concat([df13a, df13b, df13c, df13d, df13e, df13f])
df13.to_csv('user_id_87837.csv', header=True, index=False)

for i in range(len(list_start27)):
    list_start27[i] = seconds_to_time(list_start27[i])
    list_end27[i] = seconds_to_time(list_end27[i])
    list_action27[i] = 'Class ' + str(list_action27[i])
for i in range(len(list_start28)):
    list_start28[i] = seconds_to_time(list_start28[i])
    list_end28[i] = seconds_to_time(list_end28[i])
    list_action28[i] = 'Class ' + str(list_action28[i])
df14a = pd.DataFrame({'Filename': 'Dashboard_user_id_94265_5', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start27, 'End Time': list_end27, 'Label (Primary)': list_action27, 'Appearance Block': 'None'})
df14b = pd.DataFrame({'Filename': 'Dashboard_user_id_94265_7', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start28, 'End Time': list_end28, 'Label (Primary)': list_action28, 'Appearance Block': 'None'})
df14c = pd.DataFrame({'Filename': 'Rear_view_user_id_94265_5', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start27, 'End Time': list_end27, 'Label (Primary)': list_action27, 'Appearance Block': 'None'})
df14d = pd.DataFrame({'Filename': 'Rear_view_user_id_94265_7', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start28, 'End Time': list_end28, 'Label (Primary)': list_action28, 'Appearance Block': 'None'})
df14e = pd.DataFrame({'Filename': 'Right_side_window_user_id_94265_5', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start27, 'End Time': list_end27, 'Label (Primary)': list_action27, 'Appearance Block': 'None'})
df14f = pd.DataFrame({'Filename': 'Right_side_window_user_id_94265_7', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start28, 'End Time': list_end28, 'Label (Primary)': list_action28, 'Appearance Block': 'None'})
df14 = pd.concat([df14a, df14b, df14c, df14d, df14e, df14f])
df14.to_csv('user_id_94265.csv', header=True, index=False)

for i in range(len(list_start29)):
    list_start29[i] = seconds_to_time(list_start29[i])
    list_end29[i] = seconds_to_time(list_end29[i])
    list_action29[i] = 'Class ' + str(list_action29[i])
for i in range(len(list_start30)):
    list_start30[i] = seconds_to_time(list_start30[i])
    list_end30[i] = seconds_to_time(list_end30[i])
    list_action30[i] = 'Class ' + str(list_action30[i])
df15a = pd.DataFrame({'Filename': 'Dashboard_user_id_96715_5', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start29, 'End Time': list_end29, 'Label (Primary)': list_action29, 'Appearance Block': 'None'})
df15b = pd.DataFrame({'Filename': 'Dashboard_user_id_96715_7', 'Camera View': 'Dashboard', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start30, 'End Time': list_end30, 'Label (Primary)': list_action30, 'Appearance Block': 'None'})
df15c = pd.DataFrame({'Filename': 'Rear_view_user_id_96715_5', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start29, 'End Time': list_end29, 'Label (Primary)': list_action29, 'Appearance Block': 'None'})
df15d = pd.DataFrame({'Filename': 'Rear_view_user_id_96715_7', 'Camera View': 'Rearview', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start30, 'End Time': list_end30, 'Label (Primary)': list_action30, 'Appearance Block': 'None'})
df15e = pd.DataFrame({'Filename': 'Right_side_window_user_id_96715_5', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start29, 'End Time': list_end29, 'Label (Primary)': list_action29, 'Appearance Block': 'None'})
df15f = pd.DataFrame({'Filename': 'Right_side_window_user_id_96715_7', 'Camera View': 'Rightside Window', 'Activity Type': 'Distracted Behavior',
         'Start Time': list_start30, 'End Time': list_end30, 'Label (Primary)': list_action30, 'Appearance Block': 'None'})
df15 = pd.concat([df15a, df15b, df15c, df15d, df15e, df15f])
df15.to_csv('user_id_96715.csv', header=True, index=False)
