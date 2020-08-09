import re
import os
import sys
import glob
import time
import subprocess
import multiprocessing

import matplotlib.image as mpimg 
import matplotlib.pyplot as plt

def img_process (img_file, pixels):
    psnr = []
    bitrate = []
    for quality in range(0,101):
        cmd = 'cwebp -q ' + str(quality) + ' -print_psnr -short ' + img_file + ' -o ' + './out.webp'
        run_cmd = subprocess.run(cmd, shell=True, capture_output=True)
        output = re.search(r"\d+ \d+.\d+", str(run_cmd.stderr)).group(0).split(" ")
        bitrate.append(float(output[0])/pixels)
        psnr.append(float(output[1]))
    return bitrate, psnr

def main():
    start_time = time.time()
    for i in range(1, len(sys.argv)):
        current_dir = sys.argv[i]
        file_names = []
        for f in glob.glob(current_dir + "/*.png"):
            file_names.append(f)
        num_pic = len(file_names)
        img = mpimg.imread(file_names[0])
        pixels = img.shape[0] * img.shape[1]
        
        pool = multiprocessing.Pool(multiprocessing.cpu_count())
        res = pool.starmap(img_process, [(f, pixels) for f in file_names])
        pool.close()
        
        for bitrate, psnr in res:
            plt.plot(bitrate, psnr)
        plt.xlabel('Bitrate')
        plt.ylabel('PSNR')
        plt.show()
        plt.savefig(current_dir + '/metacurve.png')
        plt.clf()
    print("Done !!!")
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()