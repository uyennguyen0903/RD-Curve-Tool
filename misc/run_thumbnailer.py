import re
import os
import sys
import glob
import time
import shutil
import subprocess
import multiprocessing

def img_process (ind, pixels):
    data_file = open('./anim/' + str(ind) + '.txt', 'w+')
    
    cmd = '~/step255-2020/build/thumbnailer_compare ./thumbnailer_gen/' + str(ind) + '.txt'
    
    run_cmd = subprocess.run(cmd, shell=True, capture_output=True)
    res = str(run_cmd.stderr).replace('b','')
    res = res.replace('"','')
    ok = False
    s = ''
    for k in res:
        if (k == '\\'):
            ok = True
        else:
            if (k == 'n' and ok == True):
                ok = False
                data_file.write(s + '\n')
                s = ''
            else:
                s = s + k
    cmd = '~/step255-2020/build/thumbnailer ./thumbnailer_gen/' + str(ind) + '.txt ' + './results/' + str(ind) + 'lossy.webp'
    #print(cmd)
    run_cmd = subprocess.run(cmd, shell=True, capture_output=True)

    cmd = '~/step255-2020/build/thumbnailer ./thumbnailer_gen/' + str(ind) + '.txt ' + './results/' + str(ind) + 'slope.webp slope_optimization'
    #print(cmd)
    run_cmd = subprocess.run(cmd, shell=True, capture_output=True)
    print('Done ' + str(ind))

def main():
    start_time = time.time()
    pixels = 180*320
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    res = pool.starmap(img_process, [(ind, pixels) for ind in range(1,100)])
    pool.close()

    print("Done !!!")
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()