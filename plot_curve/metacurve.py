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
    bitrate, psnr = [], []
    tmp = img_file.replace('.png','')
    data_file = open(tmp + '-lossy.txt', 'w+')
    
    for quality in range(0,101):
        cmd = 'cwebp -q ' + str(quality) + ' -print_psnr -short ' + img_file + ' -o ' + tmp + str(quality) + '.webp'
        
        run_cmd = subprocess.run(cmd, shell=True, capture_output=True)
        output = re.search(r"\d+ \d+.\d+", str(run_cmd.stderr)).group(0).split(" ")
        
        cmd = '~/libwebp/build/get_disto ' + tmp + str(quality) + '.webp ' + img_file
        run_cmd = subprocess.run(cmd, shell=True, capture_output=True)
        output = str(run_cmd).split(' ')
        size = output[4].replace("stdout=b'",'')
        
        bitrate.append(float(size)/pixels)
        psnr.append(float(output[5]))
        
        data_file.write(str(float(size)/pixels) + ' ' + str(float(output[5])) + '\n')
    
        cmd_del = 'rm -rf ' + tmp + str(quality) + '.webp'
        run_cmd_del = subprocess.run(cmd_del, shell=True)

    data_file.close()
    return bitrate, psnr

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
        
        for bitrate, psnr in res:
            plt.plot(bitrate, psnr)
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