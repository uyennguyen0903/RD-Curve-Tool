import sys
import time
import math
import subprocess
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# f(x) = A*log(B*x)+C
def FuncLog(t, A, B, C):
    return A * np.log(B*t) + C

# f(x) = A*exp(B*x)+C
def FuncExp(t, A, B, C):
    return -A * np.exp(-B*t) + C

# f(x) = (A*x)/(B+x)
def FuncPlateau(t, A, B):
    return (A * t) / (B + t)

# f(x) = A + B*x + C*x^2 + ... + G*x^6
def FuncPoly(t, A, B, C, D, E, F, G):
    return A + B*pow(t,1) + C*pow(t,2)+ D*pow(t,3)+ E*pow(t,4)+ F*pow(t,5)+ G*pow(t,6)


def main():
    start_time = time.time()
    
    img_path = sys.argv[1]
    model = sys.argv[2]

    size = []
    psnr = []

    # Run cwebp & get_disto.
    for quality in range(0,101):
        cmd = 'cwebp -q ' + str(quality) + ' -print_psnr -short ' + img_path + ' -o tmp.webp'
        run_cmd = subprocess.run(cmd, shell=True, capture_output=True)
        
        cmd = '~/libwebp/build/get_disto ' + 'tmp.webp ' + img_path
        run_cmd = subprocess.run(cmd, shell=True, capture_output=True)
        output = str(run_cmd).split(' ')
        s = output[4].replace("stdout=b'",'')
        
        size.append(float(s))
        psnr.append(float(output[5]))
    
    ind = 3
    x = np.array ([])
    y = np.array ([])
    num_points = 0
    while ind < len(sys.argv):
        quality = int(sys.argv[ind])
        if (quality < 0 or quality > 100):
            print("Invalid quality !!!")
            sys.exit()
        x = np.append(x, [size[quality]], axis = 0)
        y = np.append(y, [psnr[quality]], axis = 0)
        plt.plot(size[quality],psnr[quality],color='red', marker='o')
        ind += 1
        num_points += 1
    
    if (num_points == 0):
        x = np.array ([size[0]])
        y = np.array ([psnr[0]])
        num_points = 7
        pas = (size[100]-size[50]) / (num_points - 2)
        cnt = 0
        plt.plot(size[0],psnr[0],color='red', marker='o')
        for i in range(51,102):
            if (i == 101 or ((size[i]-size[50]) >= cnt*pas and (size[i-1]-size[50]) <= cnt*pas)):
                cnt += 1
                plt.plot(size[i-1],psnr[i-1],color='red', marker='o')
                x = np.append(x, [size[i-1]], axis = 0)
                y = np.append(y, [psnr[i-1]], axis = 0)
                if (cnt + 1 == num_points):
                    break
    
    size = np.asarray(size, dtype = float)
    psnr = np.asarray(psnr, dtype = float)

    if (model == 'poly'):
        if (num_points >= 7):
            CurveParams, CurveCovariances = curve_fit(FuncPoly, x,y)
            plt.plot(size, FuncPoly(size, *CurveParams), color = 'sienna', label = "Polynomial curve")
        else:
            CurveParams = np.polyfit(x, y, num_points-1)
            Func = np.poly1d(CurveParams)
            plt.plot(size, Func(size), color = 'sienna', label = "Polynomial curve")
        print(CurveParams)
        
    if (model == 'log'):
        CurveParams, CurveCovariances = curve_fit(FuncLog, x,y)
        plt.plot(size, FuncLog(size, *CurveParams), color = 'sienna', label = "Logarithmic curve")
        print(CurveParams)

    plt.plot(size, psnr, color = 'blue', label = "Original R-D curve")
    plt.xlabel('Bitrate')
    plt.ylabel('PSNR')
    plt.show()
    plt.legend()
    plt.savefig(img_path.replace(".png","curve_fit.png"))
    plt.clf()

    print("Done !!!")
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()