import re
import os
import sys
import glob
import time
import shutil
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
        
        try:
            if not os.path.exists(current_dir + '/results'):
                os.makedirs(current_dir + '/results')
        except OSError:
            print ('Error: Creating directory of data')

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
        
        cmd = '~/step255-2020/build/thumbnailer ' + current_dir + '/frames.txt ' + current_dir + '/results/anim' + str(i)+ '.webp ' + current_dir + '/points.txt '
        run_cmd = subprocess.run(cmd, shell=True)

        points_file = open(current_dir + '/points.txt', "r+").readlines()
        for p in points_file:
            x = p.strip()
            final_quality = int(x)

        for bitrate, psnr in res:
            plt.plot(bitrate, psnr, color='skyblue')
            plt.plot(bitrate[final_quality], psnr[final_quality], color='green', marker='o')         

        plt.title('Lossy')
        plt.xlabel('Bitrate')
        plt.ylabel('PSNR')
        plt.show()
        plt.savefig(current_dir + '/results/lossy.png')
        plt.clf()

    print("Done !!!")
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()