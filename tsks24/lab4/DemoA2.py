import numpy as np
from scipy import signal, misc, ndimage
import cv2
from matplotlib import pyplot as plt
plt.rcParams['image.interpolation'] = 'nearest'
import jpeglab as jl
from DemoA import mse, psnr


orig = cv2.imread('image1.png')
orig = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB)


y, cb, cr = jl.rgb2ycbcr(orig)


plt.figure(1)
plt.imshow(y, 'gray', clim=(0, 255))
plt.title('y')

F = 2.0

y3 = np.floor(ndimage.zoom(y, 1.0/F, order=3))
y4 = ndimage.zoom(y3, F, order=3)
plt.figure(2)
plt.imshow(y4, 'gray', clim=(0, 255))
print(f'F={F} MSE:', mse(y, y4))
print(f'F={F} PSNR:', psnr(y, y4))
plt.show(block=False)

F = 1.5

y3 = np.floor(ndimage.zoom(y, 1.0/F, order=3))
y4 = ndimage.zoom(y3, F, order=3)
plt.figure(3)
plt.imshow(y4, 'gray', clim=(0, 255))
print(f'F={F} MSE:', mse(y, y4))
print(f'F={F} PSNR:', psnr(y, y4))
plt.show(block=False)


diff = np.abs(y - y4)
plt.figure(4)
plt.imshow(diff, 'gray', clim=(-128, 127))
plt.title('diff')
plt.show(block=True)
