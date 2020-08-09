import os
import sys
import glob
import re
import multiprocessing

import matplotlib.image as mpimg 
import matplotlib.pyplot as plt

def plot_data(data_file, pixels):
    data = open(data_file, "r+").readlines() 
    bitrate, psnr = [], []

    for i in data:
        x = i.strip().split(" ")
        bitrate.append(float(x[0])/pixels)
        psnr.append(float(x[1]))
    
    return bitrate, psnr 

def main():
    directory = sys.argv[1]
    metacurve_path = sys.argv[2]
    file_names = []
    for f in glob.glob(directory + "/data*.txt"):
        file_names.append(f)
    for f in glob.glob(directory + "/*.png"):
        img = mpimg.imread(f)
        pixels = img.shape[0] * img.shape[1]
        break
    
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    res = pool.starmap(plot_data, [(f, pixels) for f in file_names])
    pool.close()
    
    for bitrate, psnr in res:
        plt.plot(bitrate, psnr)
    plt.xlabel('Bitrate')
    plt.ylabel('PSNR')
    plt.show()
    plt.savefig(metacurve_path)
    plt.clf()

if __name__ == "__main__":
    main()