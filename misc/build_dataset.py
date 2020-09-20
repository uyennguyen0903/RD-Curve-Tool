import cv2
import numpy as np
import os
import sys
import shutil
import glob

directory = sys.argv[1]

curr_ind = 0

for video_path in glob.glob(directory + '/*.mp4'):
    num_frame = 15
    dst = video_path.replace('.mp4','')
    width = 320
    height = 180
    dim = (width,height)
    pas = 20

    capture = cv2.VideoCapture(video_path)

    try:
        if os.path.exists(dst):
            shutil.rmtree(dst)
        os.makedirs(dst)
    except OSError:
        print ('Error: Creating directory of data')

    current_frame = 0
    cnt = 0
    frames_file = open(directory + '/thumbnailer_gen/' + str(curr_ind) + '.txt', 'w+')
    timestamp = 200
    while(cnt < int(num_frame)):
        ret, frame = capture.read()
        if (current_frame % pas != 0):
            current_frame += 1
            continue
        frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
        name_frame = str(current_frame)
        while (len(name_frame) < 3):
            name_frame = '0' + name_frame
        name = dst + '/frame' + name_frame + '.png'
        frames_file.write(str(dst) + '/frame' + str(name_frame) + '.png ' + str(timestamp) + '\n')
        print(name)
        cv2.imwrite(name, frame)
        current_frame += 1
        cnt += 1

    capture.release()
    cv2.destroyAllWindows()
    print('Dumped successfully!!!')
    curr_ind += 1

