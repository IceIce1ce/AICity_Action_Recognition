import os
import numpy as np
import cv2
import torch
import torch.nn.functional as F
from models.FastFlowNet_v2 import FastFlowNet
from flow_vis import flow_to_color
import glob
from natsort import natsorted

div_flow = 20.0
div_size = 64

def centralize(img1, img2):
    b, c, h, w = img1.shape
    rgb_mean = torch.cat([img1, img2], dim=2).view(b, c, -1).mean(2).view(b, c, 1, 1)
    return img1 - rgb_mean, img2 - rgb_mean, rgb_mean

model = FastFlowNet().cuda().eval()
model.load_state_dict(torch.load('checkpoints/fastflownet_ft_mix.pth'))

path_mp4 = natsorted(glob.glob('A1_clip_fixed/0' + '/*.MP4'))
for j in range(len(path_mp4)):
    save_path_label = path_mp4[j].split('/')[1]
    save_path_folder = path_mp4[j].split('/')[-1].split('.')[0]
    print('Processing folder', save_path_label)
    if not os.path.exists('output_demo/' + str(save_path_label) + '/' + str(save_path_folder)):
        os.makedirs('output_demo/' + str(save_path_label) + '/' + str(save_path_folder))
    print('Processing video:', path_mp4[j].split('/')[-1], '\n')
    cap = cv2.VideoCapture(path_mp4[j])
    ret, first_frame = cap.read()
    cnt = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if frame is None:
            break
        img1 = torch.from_numpy(first_frame).float().permute(2, 0, 1).unsqueeze(0)/255.0
        img2 = torch.from_numpy(frame).float().permute(2, 0, 1).unsqueeze(0)/255.0
        img1, img2, _ = centralize(img1, img2)

        height, width = img1.shape[-2:]
        orig_size = (int(height), int(width))

        if height % div_size != 0 or width % div_size != 0:
            input_size = (
                int(div_size * np.ceil(height / div_size)),
                int(div_size * np.ceil(width / div_size))
            )
            img1 = F.interpolate(img1, size=input_size, mode='bilinear', align_corners=False)
            img2 = F.interpolate(img2, size=input_size, mode='bilinear', align_corners=False)
        else:
            input_size = orig_size

        input_t = torch.cat([img1, img2], 1).cuda()

        output = model(input_t).data

        flow = div_flow * F.interpolate(output, size=input_size, mode='bilinear', align_corners=False)

        if input_size != orig_size:
            scale_h = orig_size[0] / input_size[0]
            scale_w = orig_size[1] / input_size[1]
            flow = F.interpolate(flow, size=orig_size, mode='bilinear', align_corners=False)
            flow[:, 0, :, :] *= scale_w
            flow[:, 1, :, :] *= scale_h

        flow = flow[0].cpu().permute(1, 2, 0).numpy()

        flow_color = flow_to_color(flow, convert_to_bgr=True)

        cnt += 1
        first_frame = frame
        cv2.imwrite('output_demo/' + str(save_path_label) + '/' + str(save_path_folder) + '/flow_' + str(cnt) + '.jpg', flow_color)
cap.release()
cv2.destroyAllWindows()
