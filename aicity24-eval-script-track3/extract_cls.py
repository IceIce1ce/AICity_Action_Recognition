with open('GT.txt') as f:
    for line in f:
        data = line.strip().split(' ')
        video_id, labels, start_time, end_time = data[0], data[1], data[2], data[3]
        if data[1] == '11' or data[1] == '12' or data[1] == '13':
            with open('extract_cls.txt', 'a') as ft:
                ft.write(video_id + ' ' + labels + ' ' + start_time + ' ' + end_time + '\n')
