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
if len(sys.argv) == 6:
    width = sys.argv[4]
    height = sys.argv[5]
dim = (int(width), int(height))

capture = cv2.VideoCapture(video_path)

try:
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.makedirs(dst)
except OSError:
    print ('Error: Creating directory of data')

current_frame = 0
while(current_frame < int(num_frame)):
    ret, frame = capture.read()
    if width != -1 :
        frame = cv2.resize(frame, dim, interpolation = cv2.INTER_LANCZOS4)
    name_frame = str(current_frame)
    while (len(name_frame) < 3):
        name_frame = '0' + name_frame
    name = dst + '/frame' + name_frame + '.png'
    cv2.imwrite(name, frame)
    current_frame += 1

capture.release()
cv2.destroyAllWindows()
print('Dumped successfully!!!')

