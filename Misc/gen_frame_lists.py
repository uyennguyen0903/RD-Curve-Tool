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

def main():
    start_time = time.time()
    for i in range(1, 100):
        current_dir = './' + str(i)
        file_names = []
        
        timestamp = 200
        data_file = open('./thumbnailer_gen/' + str(i) + '.txt', 'w+')
        for f in glob.glob(current_dir + '/*.png'):
            file_names.append(f)
            data_file.write(f + ' ' + str(timestamp) + '\n')
            timestamp += 200

    print("Done !!!")
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()