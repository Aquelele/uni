import numpy as np
from scipy import signal, misc, ndimage
import cv2
from matplotlib import pyplot as plt
plt.rcParams['image.interpolation'] = 'nearest'
import jpeglab as jl


def mse(x,y):
    return np.mean((x-y)**2)

def psnr(x,y):
    return 10*np.log10(255**2/mse(x,y))

if __name__ == '__main__':

    orig = cv2.imread('image1.png')
    orig = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB)

    y, cb, cr = jl.rgb2ycbcr(orig)

    X = 2**3 # 8
    coded = X*np.floor_divide(y, X)

    plt.figure(1)
    plt.imshow(y, 'gray', clim=(0, 255))
    plt.title('y')

    for i in [6, 5, 4]:
        a = 8 - i
        X = 2**a
        coded = X*np.floor_divide(y, X) 
        plt.figure(i)
        plt.imshow(coded, 'gray', clim=(0, 255))
        plt.title(f'y, X={X}, a={a}, i={i}')

        print(f'i={i} MSE:', mse(y, coded))
        print(f'i={i} PSNR:', psnr(y, coded))
        plt.show(block=False)

    plt.show(block=True)

