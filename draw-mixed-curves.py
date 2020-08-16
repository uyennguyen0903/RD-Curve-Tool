import os
import sys
import glob
import re
import multiprocessing

import matplotlib.image as mpimg 
import matplotlib.pyplot as plt

def plot_data1(data_file, num):
    data = open(data_file, "r+").readlines() 
    bitrate, psnr = [], []

    for i in data:
        x = i.strip().split(" ")
        bitrate.append(float(x[0]))
        psnr.append(float(x[1]))
    
    return bitrate, psnr 

def main():
    for ii in range(1, len(sys.argv)):
        directory = sys.argv[ii]
        cnt = 0

        points_file = open(directory + '/points.txt', "r+").readlines()
        for p in points_file:
            x = p.strip()
            final_quality = int(x)

        for f in glob.glob(directory + "/frame*.png"):
            name = f.replace('.png','')
            
            bitrate, psnr = plot_data1(name+'-lossy.txt',5)
            line1 = plt.plot(bitrate, psnr, 'skyblue', label = 'Lossy')

            final_size = bitrate[final_quality]
            plt.plot(bitrate[final_quality], psnr[final_quality], color='red', marker='o', label = 'Resulting point - Lossy')

            bitrate, psnr = plot_data1(name+'-near-lossless.txt',5)
            line2 = plt.plot(bitrate, psnr, 'sienna', label = 'Near-lossless')
            plt.plot(bitrate[0], psnr[0], 'sienna')

            for ind in range(100,-1,-1):
                if (bitrate[ind] <= final_size):
                    plt.plot(bitrate[ind], psnr[ind], color='green', marker='o', label = 'Resulting point - Near-Lossless')
                    break
         
            plt.xlabel('Bitrate')
            plt.ylabel('PSNR')
            plt.legend(loc='center left', bbox_to_anchor=(0., 1.02, 1., .102), ncol=2, mode="expand")
            plt.show()
            plt.savefig(directory + '/results/' + str(cnt) + '.png')
            plt.clf()
            cnt += 1
    

if __name__ == "__main__":
    main()