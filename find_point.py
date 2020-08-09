import re
import os
import sys
import glob
import time
import subprocess
import multiprocessing

import matplotlib.image as mpimg 
import matplotlib.pyplot as plt

from metacurve import img_process

def main():
    start_time = time.time()
    for i in range(1, len(sys.argv)):
        current_dir = sys.argv[i]
        file_names = []
        
        frames_file = open(current_dir + '/frames.txt', 'w+')
        timestamp = 100
        for f in glob.glob(current_dir + '/*.png'):
            file_names.append(f)
            frames_file.write(f + ' ' + str(timestamp) + '\n')
            timestamp += 100
        frames_file.close()
        
        num_pic = len(file_names)
        img = mpimg.imread(file_names[0])
        pixels = img.shape[0] * img.shape[1]
        
        pool = multiprocessing.Pool(multiprocessing.cpu_count())
        res = pool.starmap(img_process, [(f, pixels) for f in file_names])
        pool.close()
        
        cmd = '~/step255-2020/build/thumbnailer ' + current_dir + '/frames.txt ' + current_dir + '/anim' + str(i)+ '.webp ' + current_dir + '/points.txt '
        run_cmd = subprocess.run(cmd, shell=True)

        points_file = open(current_dir + '/points.txt', "r+").readlines()
        points = []
        for p in points_file:
            x = p.strip()
            points.append(float(x))

        ind = 0
        for bitrate, psnr in res:
            plt.plot(bitrate, psnr, color='skyblue')
            num_point = int(len(points) / num_pic)
            tmp = ind
            for k in range(1,num_point+1):
                x, y = 100, 100
                for j in range(0,101):
                    if abs(psnr[j]-points[tmp])<abs(y-points[tmp]):
                        x, y = bitrate[j], psnr[j]
                tmp = tmp + num_pic
                if (k == num_point):
                    plt.plot(x, y, color='green', marker='o')
                else:
                    plt.plot(x, y, color='red', marker='o')
            ind += 1           

        plt.xlabel('Bitrate')
        plt.ylabel('PSNR')
        plt.show()
        plt.savefig(current_dir + '/metacurves' + str(i) + '.png')
        plt.clf()

    print("Done !!!")
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()