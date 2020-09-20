import cv2
import numpy as np
import os
import sys
import shutil

video_path = sys.argv[1]
num_frame = sys.argv[2]
dst = sys.argv[3]
width = -1
height = -1
width = sys.argv[4]
height = sys.argv[5]
dim = (int(width), int(height))
pas = 25

capture = cv2.VideoCapture(video_path)

try:
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.makedirs(dst)
except OSError:
    print ('Error: Creating directory of data')

current_frame = 0
cnt = 0
while(cnt < int(num_frame)):
    ret, frame = capture.read()
    if (current_frame % pas != 0):
        current_frame += 1
        continue
    if width != -1 :
        frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    name_frame = str(current_frame)
    while (len(name_frame) < 3):
        name_frame = '0' + name_frame
    name = dst + '/frame' + name_frame + '.png'
    print(name)
    cv2.imwrite(name, frame)
    current_frame += 1
    cnt += 1

capture.release()
cv2.destroyAllWindows()
print('Dumped successfully!!!')

