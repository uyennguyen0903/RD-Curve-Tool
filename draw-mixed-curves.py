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
    directory = sys.argv[1]
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
        plt.plot(bitrate[final_quality], psnr[final_quality], color='green', marker='o')

        bitrate, psnr = plot_data1(name+'-near-lossless.txt',5)
        line2 = plt.plot(bitrate, psnr, 'sienna', label = 'Near-lossless')
        
        for ind in range(100,-1,-1):
            if (bitrate[ind] <= final_size):
                plt.plot(bitrate[ind], psnr[ind], color='green', marker='o')
                break

        plt.title('Mixed RD-curves')
        plt.xlabel('Bitrate')
        plt.ylabel('PSNR')
        plt.legend()
        plt.show()
        plt.savefig(directory + '/results/' + str(cnt) + '.png')
        plt.clf()
        cnt += 1
    

if __name__ == "__main__":
    main()