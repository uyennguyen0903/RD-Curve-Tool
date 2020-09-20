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

def img_process (img_file, pixels):
    bitrate, psnr, effort = [], [], []
    tmp = img_file.replace('.png','')
    data_file = open(tmp + '-lossless.txt', 'w+')
    
    for quality in range(0,101):
        if (quality >= 50 and quality % 2 == 1):
            continue
        cmd = 'cwebp -lossless -q ' + str(quality) + ' -print_psnr -short ' + img_file + ' -o ' + './out.webp'
        run_cmd = subprocess.run(cmd, shell=True, capture_output=True)
        output = re.search(r"\d+ \d+.\d+", str(run_cmd.stderr)).group(0).split(" ")
        
        bitrate.append(float(output[0])/pixels)
        psnr.append(float(output[1]))
        effort.append(quality)
        data_file.write(str(float(output[0])/pixels) + ' ' + str(float(output[1])) + ' ' + str(quality)+'\n')
    
    data_file.close()
    return bitrate, psnr, effort

def main():
    start_time = time.time()
    for i in range(1, len(sys.argv)):
        current_dir = sys.argv[i]
        
        try:
            if not os.path.exists(current_dir + '/results'):
                os.makedirs(current_dir + '/results')
        except OSError:
            print ('Error: Creating directory of data')

        file_names = []
        for f in glob.glob(current_dir + "/*.png"):
            file_names.append(f)
        num_pic = len(file_names)
        img = mpimg.imread(file_names[0])
        pixels = img.shape[0] * img.shape[1]
        
        pool = multiprocessing.Pool(multiprocessing.cpu_count())
        res = pool.starmap(img_process, [(f, pixels) for f in file_names])
        pool.close()
        
        for bitrate, psnr, effort in res:
            plt.plot(effort, bitrate, color = 'firebrick')
        plt.title('Lossless')
        plt.xlabel('Effort')
        plt.ylabel('Bitrate')
        plt.show()
        plt.savefig(current_dir + '/results/lossless.png')
        plt.clf()
    
    print("Done !!!")
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()