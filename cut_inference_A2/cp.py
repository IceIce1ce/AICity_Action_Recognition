import glob
import shutil

path_csv = glob.glob('*.csv')
for i in range(len(path_csv)):
	file_name = path_csv[i].split('.')[0]
	shutil.move(file_name + '.csv', 'B/' + file_name + '/' + file_name + '.csv')
